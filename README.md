# pytouchok
Tkinter application for automating routine actions with GUI (similar to SikuliX and AutoIt)

The idea was to create a companion app that would track the content of the screen and, under certain conditions, take control to perform routine actions. 

As an example of such a routine action, I implemented the export of slides from LibreOffice Impress in svg format via pyautogui by automatically clicking in the interface. This operation cannot be performed for all slides through the GUI, and LibreOffice API is quite difficult to work with. 

But the main goal was to create a companion app that could be easily expanded with new skills. And it succeeded, the program "understands" that LibreOffice Impress is open on the screen and starts automatic actions. 

Here is the demo on youtube: https://www.youtube.com/watch?v=J0jYU4luY1A
