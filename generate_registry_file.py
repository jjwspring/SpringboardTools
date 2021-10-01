import sys
if sys.version_info[0] < 3:
    raise Exception("Must be using Python 3")

python_path = sys.executable
script_dir = os.path.abspath(os.path.dirname(__file__))

print (python_path)

f = open("springboard_tools.reg", "w")
f.write(r'Windows Registry Editor Version 5.00')
f.write('\n\n')
f.write(r'[HKEY_CLASSES_ROOT\*\ContextMenus]')
f.write('\n\n')
f.write(r'[HKEY_CLASSES_ROOT\*\ContextMenus\springboard]')
f.write('\n\n')
f.write(r'[HKEY_CLASSES_ROOT\*\ContextMenus\springboard\Shell]')
f.write('\n\n')
f.write(r'[HKEY_CLASSES_ROOT\*\ContextMenus\springboard\Shell\Copy Link - Full]')
f.write('\n\n')
f.write(r'[HKEY_CLASSES_ROOT\*\ContextMenus\springboard\Shell\Copy Link - Full\Command]')
f.write('\n')
f.write(r'@="\"%s\" \"%s\\copy_file_link.py\" \"%s\" Full"' % (python_path.replace("\\","\\\\"), script_dir.replace("\\", "\\\\"), "%1"))
f.write('\n\n')
f.write(r'[HKEY_CLASSES_ROOT\*\ContextMenus\springboard\Shell\Copy Link - Partial]')
f.write('\n\n')
f.write(r'[HKEY_CLASSES_ROOT\*\ContextMenus\springboard\Shell\Copy Link - Partial\Command]')
f.write('\n')
f.write(r'@="\"%s\" \"%s\\copy_file_link.py\" \"%s\" Partial"'% (python_path.replace("\\","\\\\"), script_dir.replace("\\", "\\\\"), "%1"))
f.write('\n\n')
f.write(r'[HKEY_CLASSES_ROOT\*\ContextMenus\springboard\Shell\Upissue - Draft]')
f.write('\n\n')
f.write(r'[HKEY_CLASSES_ROOT\*\ContextMenus\springboard\Shell\Upissue - Draft\Command]')
f.write('\n')
f.write(r'@="\"%s\" \"%s\\upissue.py\" \"%s\" Draft"' % (python_path.replace("\\","\\\\"), script_dir.replace("\\", "\\\\"), "%1"))
f.write('\n\n')
f.write(r'[HKEY_CLASSES_ROOT\*\ContextMenus\springboard\Shell\Upissue - Release]')
f.write('\n\n')
f.write(r'[HKEY_CLASSES_ROOT\*\ContextMenus\springboard\Shell\Upissue - Release\Command]')
f.write('\n')
f.write(r'@="\"%s\" \"%s\\upissue.py\" \"%s\" Release"' % (python_path.replace("\\","\\\\"), script_dir.replace("\\", "\\\\"), "%1"))
f.write('\n\n')
f.write(r'[HKEY_CLASSES_ROOT\*\shell\springboard_anchor]')
f.write('\n')
f.write(r'"MUIVerb"="Springboard"')
f.write('\n')
f.write(r'"ExtendedSubCommandsKey"="*\\\\ContextMenus\\\\springboard"')


f.close()

input()
