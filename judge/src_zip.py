import zlib

def zip_src(src):
 compression_level = 9 # Max Compression

 # We prefer that compressed source not end in a quotation mark
 compressed = zlib.compress(src, compression_level, wbits=-zlib.MAX_WBITS)

 def sanitize_for_quote_type(b_in, quote_type):
  """Clean up problematic bytes in compressed b-string for specific quote type"""
  b_out = bytearray()
  for i, b in enumerate(b_in):
   if b==0:
    # If the next character is [0-9], use \\x00 instead of \\0
    if i+1<len(b_in) and chr(b_in[i+1]).isdigit(): b_out += b"\\x00"
    else: b_out += b"\\0"
   elif b==ord("\r") and (quote_type == "'" or quote_type == '"'): b_out += b"\\r"
   elif b==ord("\\"): b_out += b"\\\\"
   elif b==ord("\n") and (quote_type == "'" or quote_type == '"'): b_out += b"\\n"
   elif quote_type == "'" and b==ord("'"): b_out += b"\\'"
   elif quote_type == '"' and b==ord('"'): b_out += b'\\"'
   else: b_out.append(b)
  return b"" + b_out

 def check_triple_quote_escape(b_in, quote_char):
  """Check if triple quote sequence needs escaping"""
  quote_byte = ord(quote_char)
  triple_pattern = bytes([quote_byte, quote_byte, quote_byte])
  if triple_pattern in b_in:
   # Need to escape triple quotes
   b_out = bytearray()
   i = 0
   while i < len(b_in):
    if i <= len(b_in) - 3 and b_in[i:i+3] == triple_pattern:
     # Found triple quote, escape the last one
     b_out.extend(b_in[i:i+2])
     b_out += b"\\" + bytes([quote_byte])
     i += 3
    else:
     b_out.append(b_in[i])
     i += 1
   return b"" + b_out
  return b_in

 # Try all quote types and find the shortest result
 options = []
 
 # Option 1: Single quotes with escaping
 sanitized_single = sanitize_for_quote_type(compressed, "'")
 result_single = b"#coding:L1\nimport zlib\nexec(zlib.decompress(bytes('" + sanitized_single + b"','L1'),-8))"
 options.append(result_single)
 
 # Option 2: Double quotes with escaping  
 sanitized_double = sanitize_for_quote_type(compressed, '"')
 result_double = b"#coding:L1\nimport zlib\nexec(zlib.decompress(bytes(\"" + sanitized_double + b'","L1"),-8))'
 options.append(result_double)
 
 # Option 3: Triple single quotes
 base_sanitized = bytearray()
 for i,b in enumerate(compressed):
  if   b==0:
   if i+1<len(compressed) and chr(compressed[i+1]).isdigit(): base_sanitized += b"\\x00"
   else: base_sanitized += b"\\0"
  elif b==ord("\r"): base_sanitized += b"\\r"
  elif b==ord("\\"): base_sanitized += b"\\\\"
  else: base_sanitized.append(b)
 base_sanitized = b"" + base_sanitized
 
 sanitized_triple_single = sanitize_for_quote_type(base_sanitized, "'''")
 result_triple_single = b"#coding:L1\nimport zlib\nexec(zlib.decompress(bytes('''" + sanitized_triple_single + b"''','L1'),-8))"
 options.append(result_triple_single)
 
 # Option 4: Triple double quotes (original logic)
 sanitized_triple_double = sanitize_for_quote_type(base_sanitized, '"""')
 result_triple_double = b"#coding:L1\nimport zlib\nexec(zlib.decompress(bytes(\"\"\"" + sanitized_triple_double + b'"""","L1"),-8))'
 options.append(result_triple_double)
 
 # Return the shortest option
 return min(options, key=len)