"""Lets make a Sim!"""
from tkinter import *
import sel


# noinspection PyShadowingNames,PyPep8Naming
def startingcas():
    root = Tk()
    startCAS = Label(root, text="Sul sul! Happy days Simmer! Lets make some Sims!")

    def click1():
        root2 = Tk()
        var = root.withdraw
        parents = Label(root2, text="Does this Sim have pre-existing parents?")
        parents.grid()
        root2.title("Create a Sim")

        def clicknp():
            root3 = Tk()
            root2.withdraw()
            import parentlessselections as sel
            toddler = Label(root3, text="As a toddler my parents would say I was " + str(sel.ttrait) + ".")
            child = Label(root3,
                          text="As I grew up I found I " + str(sel.childt1) + " and " + str(sel.childt2) + ".")
            adult = Label(root3, text="I've grown to find I'm also " + str(sel.adults) + ".")
            quitthis = Button(root3, text="Quit", command=quit)
            root3.title("Create a Sim")
            toddler.grid(), child.grid(), adult.grid(), quitthis.grid()

        def clickyp():
            root4 = Tk()
            root2.withdraw()
            oops = Label(root4, text="Oops sorry this hasnt been configured!")
            quitthat = Button(root4, text="Exit", command=quit)
            rewind = Button(root4, text="Go Back", command=click1)
            root4.title("Create a Sim")
            oops.grid(), rewind.grid(), quitthat.grid()

        confbttn = Button(root2, text="Yes", command=clickyp)
        denybttn = Button(root2, text="No", command=clicknp)
        confbttn.grid(), denybttn.grid(),

    casBttn = Button(root, text="Let's go!", command=click1)
    quitCAS = Button(root, text="Bye!", command=quit)
    root.title("Create a Sim")
    startCAS.grid(), casBttn.grid(), quitCAS.grid()
    root.mainloop()


startingcas()
