import os
import markdown

contentDir = r''           # Markdown file directory
outputDir = r''            # Output directory
templateFile = r''         # HTML template file

def readTemplate(path):
    if not os.path.exists(path):
        raise FileNotFoundError(f"Template file '{path}' does not exist.")
    with open(path, 'r') as file:
        return file.read()

def convertMarkdownToHTML(markdownText):
    return markdown.markdown(markdownText)

def generateHTML(markdownFile, templateContent, outputPath):
    with open(markdownFile, 'r') as file:
        markdownContent = file.read()
        print(f"Read markdown content from {markdownFile}:\n{markdownContent[:100]}...")
    htmlContent = convertMarkdownToHTML(markdownContent)
    completeHtml = templateContent.replace('{{ content }}', htmlContent)
    outputFilePath = os.path.join(outputPath, os.path.splitext(os.path.basename(markdownFile))[0] + '.html')
    
    # Debugging statements
    print(f"Writing to: {outputFilePath}")
    
    with open(outputFilePath, 'w') as file:
        file.write(completeHtml)
        print(f"Successfully wrote HTML file to {outputFilePath}")

def main():
    absoluteOutputDir = os.path.abspath(outputDir)    
    if not os.path.exists(absoluteOutputDir):
        os.makedirs(absoluteOutputDir)
    
    print(f"Reading template file from: {templateFile}")
    templateContent = readTemplate(templateFile)
    
    print(f"Searching for markdown files in: {contentDir}")
    for root, _, files in os.walk(contentDir):
        for file in files:
            if file.endswith('.md'):
                markdownFile = os.path.join(root, file)
                print(f"Processing file: {markdownFile}")
                generateHTML(markdownFile, templateContent, absoluteOutputDir)
                print(f"Generated HTML for {markdownFile}")

    print(f"HTML files are generated in: {absoluteOutputDir}")

if __name__ == '__main__':
    main()
