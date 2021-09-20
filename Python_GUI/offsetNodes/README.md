# removeInput

offset nodes in the Node Graph.

### HOW TO USE IT

* Select node(s).
* Edit -> Offset upstream
or
* Edit -> Offset downstream

### RESULT

* Selected nodes are shifted above their first input or below their first output in the Node Graph.

### SHORTCUT

* Ctrl+up arrow
or
* Ctrl+up arrow

### INSTALLATION

* Copy 'offsetNodes' folder in your .Natron folder.
* Add following lines to your 'initGui.py' file, where ``<path>`` is the location of 'removeInput' folder.

```
from <path>.offsetNodes.offsetNodes import *
NatronGui.natron.addMenuCommand('Edit/Offset Up','offsetNodes(True)', QtCore.Qt.Key.Key_Up, QtCore.Qt.KeyboardModifier.AltModifier)
NatronGui.natron.addMenuCommand('Edit/Offset Down','offsetNodes(False)', QtCore.Qt.Key.Key_Down, QtCore.Qt.KeyboardModifier.AltModifier)
```
