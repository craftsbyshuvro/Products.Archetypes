from debug import log
from Products.generator.widget import macrowidget

from utils import capitalize

class TypesWidget(macrowidget):
    _properties = macrowidget._properties.copy()
    _properties.update({
        'modes' : ('view', 'edit'),
        })

    def bootstrap(self, instance):
        macros = macrowidget.bootstrap(self, instance)

        if not self.description or not self.label:
            field = self.findField(instance)
            name = field.name
            if not self.description:
                self.description = "Enter a value for %s" % name
            if not self.label:
                self.label = capitalize(name)

        return macros
                
    def findField(self, instance):
        #This is a sad hack, I don't want widgets to have to take a
        #reference to a field or its own name
        for field in instance.type.fields():
            if not hasattr(field, 'widget'):
                continue
            if field.widget is self:
                return field
        return None


class StringWidget(TypesWidget):
    _properties = TypesWidget._properties.copy()
    _properties.update({
        'macro' : "here/widgets/string"
        })

class FloatWidget(TypesWidget):
    _properties = TypesWidget._properties.copy()
    _properties.update({
        'macro' : "here/widgets/float",
        'size' : '5',
        })

class IntegerWidget(TypesWidget):
    _properties = TypesWidget._properties.copy()
    _properties.update({
        'macro' : "here/widgets/integer",
        'size' : '5',
        })

class TextAreaWidget(TypesWidget):
    _properties = TypesWidget._properties.copy()
    _properties.update({
        'macro' : "here/widgets/textarea",
        'rows'  : 5,
        'cols'  : 40,
        'format': 0,
        })

class LinesWidget(TypesWidget):
    _properties = TypesWidget._properties.copy()
    _properties.update({
        'macro' : "here/widgets/lines",
        'rows'  : 5,
        'cols'  : 40,
        })
    
class BooleanWidget(TypesWidget):
    _properties = TypesWidget._properties.copy()
    _properties.update({
        'macro' : "here/widgets/boolean",
        })
    
class CalendarWidget(TypesWidget):
    _properties = TypesWidget._properties.copy()
    _properties.update({
        'macro' : "here/widgets/calendar",
        })

class SelectionWidget(TypesWidget):
    _properties = TypesWidget._properties.copy()
    _properties.update({
        'macro' : "here/widgets/selection",
        })

class MultiSelectionWidget(TypesWidget):
    _properties = TypesWidget._properties.copy()
    _properties.update({
        'macro' : "here/widgets/multiselection",
        'size'  : 5,
        })
    
class KeywordWidget(TypesWidget):
    _properties = TypesWidget._properties.copy()
    _properties.update({
        'macro' : "here/widgets/keyword",
        'size'  : 5,
        })

class RichWidget(TypesWidget):
    _properties = TypesWidget._properties.copy()
    _properties.update({
        'macro' : "here/widgets/rich",
        'rows'  : 5,
        'cols'  : 40,
        'format': 1,
        })

class FileWidget(TypesWidget):
    _properties = TypesWidget._properties.copy()
    _properties.update({
        'macro' : "here/widgets/file",
        })

class IdWidget(TypesWidget):
    _properties = TypesWidget._properties.copy()
    _properties.update({
        'macro' : "here/widgets/zid",
        })

class ImageWidget(TypesWidget):
    _properties = TypesWidget._properties.copy()
    _properties.update({
        'macro' : "here/widgets/image",
        })



