from abc import ABC, abstractmethod

class LocalizerFactory(ABC):
    """
    Abstract Creator: Defines the Factory Method to create localizers.
    
    This is an abstract class defining the interface for concrete localizer factories.
    """
    
    @abstractmethod
    def create_localizer(self):
        pass


class FrenchLocalizerFactory(LocalizerFactory):
    """
    Concrete Creator: Creates FrenchLocalizer instances.
    
    This class creates FrenchLocalizer instances using the Factory Method.
    """
    
    def create_localizer(self):
        return FrenchLocalizer()


class SpanishLocalizerFactory(LocalizerFactory):
    """
    Concrete Creator: Creates SpanishLocalizer instances.
    
    This class creates SpanishLocalizer instances using the Factory Method.
    """
    
    def create_localizer(self):
        return SpanishLocalizer()


class EnglishLocalizerFactory(LocalizerFactory):
    """
    Concrete Creator: Creates EnglishLocalizer instances.
    
    This class creates EnglishLocalizer instances using the Factory Method.
    """
    
    def create_localizer(self):
        return EnglishLocalizer()

class Localizer(ABC):
    """
    Abstract Product: Represents translations for specific languages.
    
    This is an abstract class defining the interface for concrete localizers.
    """
    
    @abstractmethod
    def localize(self, msg):
        pass

class FrenchLocalizer(Localizer):
    """
    Concrete Product: Represents translations for French.
    
    This class provides translations for French language.
    """
    
    def __init__(self):
        self.translations = {
            "car": "voiture",
            "bike": "bicyclette",
            "cycle": "cyclette"
        }

    def localize(self, msg):
        return self.translations.get(msg, msg)


class SpanishLocalizer(Localizer):
    """
    Concrete Product: Represents translations for Spanish.
    
    This class provides translations for Spanish language.
    """
    
    def __init__(self):
        self.translations = {
            "car": "coche",
            "bike": "bicicleta",
            "cycle": "ciclo"
        }

    def localize(self, msg):
        return self.translations.get(msg, msg)


class EnglishLocalizer(Localizer):
    """
    Concrete Product: Represents translations for English.
    
    This class provides translations for the English language.
    """
    
    def localize(self, msg):
        return msg
    
if __name__ == "__main__":
    # Create Factory instances for different languages
    french_factory = FrenchLocalizerFactory()
    english_factory = EnglishLocalizerFactory()
    spanish_factory = SpanishLocalizerFactory()

    message = ["car", "bike", "cycle"]

    # Create and use localizers without knowing the concrete classes
    french_localizer = french_factory.create_localizer()
    english_localizer = english_factory.create_localizer()
    spanish_localizer = spanish_factory.create_localizer()

    for msg in message:
        # Translate and print the messages
        print(f"Message: {msg}")
        print(f"French: {french_localizer.localize(msg)}")
        print(f"English: {english_localizer.localize(msg)}")
        print(f"Spanish: {spanish_localizer.localize(msg)}")
        print("-" * 30)

"""
This version uses Python's ability to store functions and classes as variables. 
Simplify object creation by storing Factory Methods as dictionary values, 
indexed by language parameters. Provide the desired language parameter to create 
localizers without separate concrete factory classes.
"""
# def create_localizer(language="English"):
#     """
#     Factory Method: Create a localizer for the specified language.
#     """
#     localizers = {
#         "French": FrenchLocalizer,
#         "English": EnglishLocalizer,
#         "Spanish": SpanishLocalizer,
#     }
#     return localizers[language]()

# if __name__ == "__main__":
#     # Create localizers for different languages
#     french_localizer = create_localizer("French")
#     english_localizer = create_localizer("English")
#     spanish_localizer = create_localizer("Spanish")

#     message = ["car", "bike", "cycle"]

#     for msg in message:
#         # Translate and print the messages
#         print(f"Message: {msg}")
#         print(f"French: {french_localizer.localize(msg)}")
#         print(f"English: {english_localizer.localize(msg)}")
#         print(f"Spanish: {spanish_localizer.localize(msg)}")
#         print("-" * 30)