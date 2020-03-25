#sulime text plugin to underline words with stars

import sublime, sublime_plugin
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
