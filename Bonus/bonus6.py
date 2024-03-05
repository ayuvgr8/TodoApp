contents = ["Hi,How you doin ?", "The files reported on DMS", "Presented the Pitch in front of the Sharks"]

filenames = ["docs.txt", "reports.txt", "presentation.txt"]

for content, filename in enumerate(filenames):
    file = open(f"../files/{filename}", "w")
    file.write(content)