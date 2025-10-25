class AreaOfKnowledge:
    spells = {} #'spell_name':spell_func
    modifiers = {} #'mod_name':mod_func
    classifiers = {} #'class_name':class_func
    def __init__(self, name):
        self.name = name
