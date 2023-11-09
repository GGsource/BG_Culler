# BG_Culler Tool
# Author: GGSource
# Creation Date: 11/9/2023
# Tool Functionality: This tool takes a directory containing background images and
# takes the 10 smallest images and prints their names as a list. The user can open the images,
# delete them, or exit.
# Tool Purpose: This is intended to help enforce a minimum resolution for background images by
# helping the user easily find and delete images that are too small, which they might have missed.

# Import statements
import os
import PIL.Image

# Save the path to the directory containing the images. User should modify this to their own directory.
bgDirectory = "M:\OneDrive\Images\DesktopBGs"
# Go through the directory, keeping track of only the 10 smallest resolution images.
imageList = []

# Function to get the resolution of an image.


def getImageResolution(imagePath):
    # Open the image and get the resolution with the PIL library.
    image = PIL.Image.open(imagePath)
    return image.size  # Return the resolution as a tuple.

# Print the list of images, with their resolutions. Also normalize the printed string so all the resolutions are aligned, 50 characters from the start of the string. Indices at the start of the string are also printed.


def printSmallestImages(sourceList):
    print("The 10 smallest images in the directory are: ")
    print("------------------------------------------------------------------")
    for image in sourceList:
        print(str(sourceList.index(image)) + ". " +
              image[0] + " " * (50 - len(image[0])) + str(image[1]))
        print("------------------------------------------------------------------")

# Function to populate the list of smallest images.


def populateSmallestImages(directory, targetList):
    targetList.clear()  # Clear the list of images to start fresh.
    for image in os.listdir(directory):
        if image.endswith(".jpg") or image.endswith(".png"):
            # Get the resolution of the image manually.
            imageResolution = getImageResolution(
                os.path.join(directory, image))
            # imageResolution is a tuple
            # If the list is empty, add the image to the list.
            if len(targetList) == 0:
                targetList.append([image, imageResolution])
            else:
                # If the list isn't empty, check if the image is smaller than the smallest image in the list.
                # If it is, add it to the list and sort the list.
                if imageResolution[0] < targetList[0][1][0] and imageResolution[1] < targetList[0][1][1]:
                    targetList.append([image, imageResolution])
                    targetList.sort(key=lambda x: x[1][0])
                    targetList.sort(key=lambda x: x[1][1])
                    # If the list is longer than 10, remove the last item.
                    if len(targetList) > 10:
                        targetList.pop()
    printSmallestImages(targetList)


populateSmallestImages(bgDirectory, imageList)

# Ask the user if they want to open the images, delete them, or exit through the use of commands.
# o imageIndex - Open the image at the given index as it appears in the list.
# r imageIndex - Remove the image at the given index as it appears in the list. Also recreate the list, so the user can see the new smallest images.
# f imageIndex - Open the folder in file explorer with this image selected in it.
# x - Exit the program.

while True:
    command = input("Enter a command: ")
    if command == "x":
        break
    # TODO: This opens the file but it is not in focus. Fix this.
    elif command[0] == "o":
        imageIndex = int(command[2:])
        os.startfile(os.path.join(bgDirectory, imageList[imageIndex][0]))
    # TODO: This opens the folder, but the image is not selected. Fix this.
    elif command[0] == "f":
        imageIndex = int(command[2:])
        os.startfile(bgDirectory)
    elif command[0] == "r":  # FIXME: Indices starting at 0 could be confusing.
        imageIndex = int(command[2:])
        os.remove(os.path.join(bgDirectory, imageList[imageIndex][0]))
        populateSmallestImages(bgDirectory, imageList)
    else:
        print("Invalid command. Please try again.")


# TODO: Create a GUI for this tool.
