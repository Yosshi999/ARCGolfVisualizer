import interegular
import interegular.fsm

__all__ = ["Terminal", "RESERVED", "RegexTerminal", "NAME", "NUMBER", "confusion_check"]

class Terminal:
    def __init__(self, value: str):
        self.value = value
    
class RESERVED(Terminal):
    pass

regex_patterns = {
    "NAME": "[^\\W\\d]\\w*",
    "NUMBER": "(\\d+(\\.\\d*)?|\\.\\d+)([eE][+-]?\\d+)?j?",
}

regex_fsms = {}
live_states = {}
for name, pattern in regex_patterns.items():
    fsm = interegular.parse_pattern(pattern).to_fsm()
    live_states[name] = set(filter(fsm.islive, fsm.states))
    regex_fsms[name] = fsm

class RegexTerminal(Terminal):
    name: str
    def __init__(self, value: str):
        super().__init__(value)
        assert regex_fsms[self.name].accepts(value), f"Value '{value}' does not match regex {self.name}"

class NAME(RegexTerminal):
    name: "NAME"

class NUMBER(RegexTerminal):
    name: "NUMBER"

def alive(self: interegular.FSM, lives, test: str):
    state = self.initial
    for symbol in test:
        if interegular.fsm.anything_else in self.alphabet and not symbol in self.alphabet:
            symbol = interegular.fsm.anything_else
        transition = self.alphabet[symbol]

        # Missing transition = transition to dead state
        if not (state in self.map and transition in self.map[state]):
            return False

        state = self.map[state][transition]
    return state in lives

def confusion_check(term1: Terminal, term2: Terminal) -> bool:
    test = term1.value + term2.value[0]
    for name in regex_fsms.keys():
        if alive(regex_fsms[name], live_states[name], test):
            # Potensial confusion
            return True
    return False

if __name__ == "__main__":
    print("return123", confusion_check(RESERVED("return"), NUMBER("123")))
    print("123if", confusion_check(NUMBER("123"), RESERVED("if")))
    print("123else", confusion_check(NUMBER("123"), RESERVED("else")))