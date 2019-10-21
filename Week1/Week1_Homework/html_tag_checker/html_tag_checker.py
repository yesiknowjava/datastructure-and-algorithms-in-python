class HtmlStackClass:

    # Class takes in a list when initialized
    def __init__(self):
        self.stack = []
        self.pairs = {
            '<html': '</html>',
            '<head': '</head>',
            '<title': '</title>',
            '<script': '</script>',
            '<br': '</br>',
            '<body': '</body>',
            '<a': '</a>',
            '<p': '</p>',
            '<table': '</table>',
            '<tr': '</tr>',
            '<td': '</td>',
            '<th': '</th>',
            '<select': '</select>',
        }
        self.singles = [
            '<link', '<meta', '<!doctype'
        ]

    def tags_in_line(self, line, list_values):
        for item in list_values:
            if item in line:
                return item
        return False

    def is_single_tag(self, line, list_values):
        for item in list_values:
            if item in line:
                return True
        return False
    def isEmpty(self):
        return True if self.stack == [] else False

    def pattern_match(self, begin_tag, end_tag):
        if self.pairs[begin_tag] == end_tag:
            return True
        else:
            return False

    def push(self, item):
        self.stack.insert(0,item)

    def pop(self):
        if self.stack:
            return self.stack.pop(0)            
        else:
            return None

if __name__ == '__main__':
    print("Program to check html tag closing")
    file = open('html_file.html')
    stack = HtmlStackClass()
    tag_matches = True
    lines = file.readlines()
    opening_tags = stack.pairs.keys()
    closing_tags = stack.pairs.values()
    for line in lines:
        opening_tag = stack.tags_in_line(line, opening_tags)
        closing_tag = stack.tags_in_line(line, closing_tags)
        
        if stack.is_single_tag(line, stack.singles) == False:

            if opening_tag and closing_tag:
                if stack.pairs[opening_tag] != closing_tag:
                    tag_matches = False
            else:
                if opening_tag:
                    stack.push(opening_tag)
                elif closing_tag:
                    if stack.isEmpty():
                        tag_matches = False
                    else:
                        if not stack.pattern_match(stack.pop(), closing_tag):
                            tag_matches = False
        
        
    if tag_matches and stack.isEmpty():
        print("Tag Match Perfecto")
    else:
        print("Tag does not match!!")
    file.close()

       


