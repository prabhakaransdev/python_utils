#sublime create plugins:
#***********************
#https://www.sublimetext.com/docs/plugin-examples
#
#working plugin
#**************
#create a new plugin using Tools-->Developer--> New Plugin and add the below code. Then create the key binding to create a shortcut to call the new plugin.

import sublime, sublime_plugin
#plugin to underline words with stars

class StarsCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        #text selection
        for region in self.view.sel():
            if not region.empty():
                #get the selected text
                s = self.view.substr(region)
                #transform it by adding stars under the selectedLine
                starlen = len(s)
                stars = ''
                for i in range(starlen):
                    stars = stars+'*'
                s = s+'\n'+stars
                #replace the selection with transformed text
                self.view.replace(edit,region, s)

#key_binding:
#************
[
	{ "keys": ["ctrl+8"], "command": "stars" }
]
