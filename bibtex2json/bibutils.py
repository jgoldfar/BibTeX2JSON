import re

allBeforeComment = re.compile('([^%]*?)%')
def cleanInputLine(line):
    line = line.strip()
    if line == '' or (line.startswith('%')):
        return ''
    if '%' in line:
        result = re.match(allBeforeComment, line)
        line = result.group(1)
    return line

entryStartPattern = re.compile('@(\w+)\{\w+')
def findEntries(lines):
    return [i for i, line in enumerate(lines) if re.match(entryStartPattern, line)]
    
def extractEntries(lines):
    entriesIndices = findEntries(lines)
    entriesIndices.append(len(lines))
    return [' '.join(lines[start:end]) for start, end in zip(entriesIndices[0:-1], entriesIndices[1:len(entriesIndices)])]
    