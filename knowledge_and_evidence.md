# Evidence and Knowledge

This document includes instructions and knowledge questions that must be completed to receive a *Competent* grade on this portfolio task.

## 1. Required evidence

### 1.1. Answer all questions in this document

- Each answer should be complete, well-articulated, and within the specified word count limits (if added) for each question.
- Please make sure **all** external sources are properly cited.
- You must **use your own words**. Please include your full chat transcripts if you use generative AI in any way.
- Generative AI hallucinates, is not an authoritative source

### 1.2. Make all the required modifications to the code

- Please follow the instructions in this document to make the changes needed to the code.

- When requested to upload evidence, upload all screenshots to `screenshots/` and embed them in this document. For example:

```markdown
![Example Running Code](screenshots/screenshot1.png)
```

![Sample](screenshots/sample.png)
> Note the `!`, and the use of a relative path.

- You must upload the code into your GitHub repository.
- While you can use a branch, your code should be in main when you submit.
- Upload a zip of this repository to Blackboard when you are ready to submit.
- You will be notified of your result via Blackboard
- However, if using GitHub classrooms, you may also receive additional feedback on GitHub directly

### 1.3. Optional: Use of Raspberry Pi and SenseHat

Raspberry Pi or SenseHat is **optional** for this activity. You can use the included `sense_hat.py` file to simulate the SenseHat on your computer.

If you use a Pi, please **delete** the `sense_hat.py` file.

### 1.4. Accessible version of the code

This project relies on visual patterns that appear on an LED matrix. If you have any accessibility requirements, you can use the `udl/accessible` branch to complete the project. This branch provides an accessible code version that uses text-based patterns instead of visual ones.

Please discuss this with your lecturer before using that branch.

## 2. Specific Tasks & Questions

Address the following tasks and questions based on the code provided in this repository.

### 2.1. Set up the project locally

1. Fork this repository (if not using GitHub Classrooms)
2. Clone your repository locally
3. Run the project locally by executing the `main.py` file
4. Evidence this by providing screenshots of the project directory structure and the output of the `main.py` file

<img width="567" height="70" alt="image" src="https://github.com/user-attachments/assets/bbc627c9-437e-4e53-b180-7852f02ee6e1" />


If you are running on a Raspberry Pi, you can use the following command to run the project and then screenshot the result:

```bash
ls
python3 main.py
```

### 2.2. Fundamental code comprehension

 Answer each of the following questions **as they relate to that code** supplied by in this repository (ignore `sense_hat.py`):

1. Examine the code for the `smiley.py` file and provide  an example of a variable of each of the following types and their corresponding values (`_` should be replaced with the appropriate values):

   | Type                    | name       | value          |
   | ----------              | ---------- | -------------- |
   | built-in primitive type | dimmed     |  True          |
   | built-in composite type | Y          |  self.YELLOW   |
   | user-defined type       | Smiley     |  _             |

2. Fill in (`_`) the following table based on the code in `smiley.py`:

   | Object                   | Type                    |
   | ------------             | ----------------------- |
   | self.pixels              | list                    |
   | A member of self.pixels  | index                   |
   | self                     | function                |

3. Examine the code for `smiley.py`, `sad.py`, and `happy.py`. Give an example of each of the following control structures using an example from **each** of these files. Include the first line and the line range:

   | Control Flow | File       | First line  | Line range  |
   | ------------ | ---------- | ----------- | ----------- |
   |  sequence    | happy.py   | 39          | 39-43       |
   |  selection   | sad.py     | 26          | 26-29       |
   |  iteration   | sad.py     | 16          | 16-17       |

4. Though everything in Python is an object, it is sometimes said to have four "primitive" types. Examining the three files `smiley.py`, `sad.py`, and `happy.py`, identify which of the following types are used in any of these files, and give an example of each (use an example from the code, if applicable, otherwise provide an example of your own):

   | Type                    | Used? | Example |
   | ----------------------- | ----- | --------|
   | int                     | Yes   | mouth = [49...  |
   | float                   | Yes   | delay=0.25      |
   | str                     | No    | ("Hello World") |
   | bool                    | Yes   | wide_open=True  |

5. Examining `smiley.py`, provide an example of a class variable and an instance variable (attribute). Explain **why** one is defined as a class variable and the other as an instance variable.

> YELLOW is an example of a class variable, and that __init__(self) . The reason that YELLOW is considered a class variable is that it is a variable that is shared across all instances of that class - say if you were to run the the happy.py or sad.py files, it would still borrow the exact same settings for YELLOW from the Smiley class. On the other hand __init__(self) is an instance variable in that this property is not shared by all other instances of the class.
>

6. Examine `happy.py`, and identify the constructor (initializer) for the `Happy` class:
   1. What is the purpose of a constructor (in general) and this one (in particular)?

   > The purpose of a constructor is to initialize setting up an object by manually defining its state and attributes for the purposes of object-oriented programming (OOP)
   > The constructor in the happy.py file is the class Happy (Smiley, Blinkable) which is set up to defund the Happy class as its own object, borrowing from the Smiley and Blinkable classes.
   >

   2. What statement(s) does it execute (consider the `super` call), and what is the result?

   > It executes the happy script from happy.py, which initialises a version of smiley with a happy setting. You will also be greeted with a print statement that says: Starting mock SenseHAT
   >

### 2.3. Code style

1. What code style is used in the code? Is it likely to be the same as the code style used in the SenseHat? Give to reasons as to why/why not:

> The code conforms to the PEP8 style guide. It is likely to be the same as the code style used in SenseHAT. The reason why both codes are written in the PEP8 style is that PEP8 is a common standard adopted by many programmers in order to have the most cleanest and concise code for others to read and modify.
>

2. List three aspects of this convention you see applied in the code.

> - Four space indentation
> - The closing brace/bracket/parenthesis on multiline constructs may either line up under the first non-whitespace character of the last line of list
> - Flowing long blocks of text with fewer structural restrictions (docstrings or comments), the line length should be limited to 72 characters.

3. Give two examples of organizational documentation in the code.

> """Demonstrates the use of the Smiley class and its subclasses.
If you have access to a SenseHAT (either via a Raspberry Pi or a SenseHAT emulator), you can use the real SenseHAT class instead of the mock SenseHAT class.
That is, delete the sense_hat.py file that is included in this bundle."""

> """
        Set the SenseHat's light intensity to low (True) or high (False)
        :param dimmed: Dim the display if True, otherwise don't dim
        """

### 2.4. Identifying and understanding classes

> Note: Ignore the `sense_hat.py` file when answering the questions below

1. List all the classes you identified in the project. Indicate which classes are base classes and which are subclasses. For subclasses, identify all direct base classes.
  
  Use the following table for your answers:

| Class Name | Super or Sub? | Direct parent(s) |
| ---------- | ------------- | ---------------- |
| Smiley     | Super         |                  |
| Happy      | Sub           | Smiley           |
| Sad        | Sub           | Smiley           |
| Blinkable  | Sub           | Smiley           |
| SenseHat   | Super         |                  |

2. Explain the concept of abstraction, giving an example from the project (note "implementing an ABC" is **not** in itself an example of abstraction). (Max 150 words)

> Abstraction, in the context of object-oriented programming, is the combination of methods and properties into a class, so that the user can just call the class, without knowing any (let alone, all) of the details of how it actually functions
> The abstraction example in the project is the smiley face on the light boards. The smiley is an abstract representation of a human face. The internal details of the smiley is actually made of circuitry and LEDs

3. What is the name of the process of deriving from base classes? What is its purpose in this project? (Max 150 words)

> Inheritance is the process of deriving from base classes. The purpose of inheritance in the project is to configure the various different 'moods' (subclasses - happy / sad) of the Smiley superclass.
>

### 2.5. Compare and contrast classes

Compare and contrast the classes Happy and Sad.

1. What is the key difference between the two classes?
   > There is additional blinkable class property in the happy class (inherited from blinkable class)
   >
2. What are the key similarities?
   > Both (sub)classes have def__init__(self):, def draw_mouth(self):, def draw_eyes functions. They also both need to import the smiley function from smiley.py
   >
3. What difference stands out the most to you and why?
   > The blinkable class property in the happy class stands out the most to me, as it adds a function that doesn't exist in the default smiley property.
   >
4. How does this difference affect the functionality of these classes
   > The sad class doesn't have the blinkable property, so it loses one functionality. 
   >

### 2.6. Where is the Sense(Hat) in the code?

1. Which class(es) utilize the functionality of the SenseHat?
   > The Smiley class directly imports SenseHat's functionality into its own code.
   >
2. Which of these classes directly interact with the SenseHat functionalities?
   > The Smiley class directly interacts with SenseHat's functionalities as it actually references SenseHat 
   >
3. Discuss the hiding of the SenseHAT in terms of encapsulation (100-200 Words)
   > SenseHat's encapsulation is demonstrated by hiding its internal operations, such as the LED matrix and sensors. Instead of directly interacting with the hardware to produce new assertions, users can change the parameters within the libraries, without having to understand the hardware side. Thus, SenseHat's encapsulation promotes cleaner, safer and reliable code interaction.
   >

### 2.7. Sad Smileys Can’t Blink (Or Can They?)

Unlike the `Happy` smiley, the current implementation of the `Sad` smiley does not possess the ability to blink. Let's first explore how blinking has been implemented in the Happy Smiley by examining the blink() method, which takes one argument that determines the duration of the blink.

**Understanding Blink Mechanism:**

1. Does the code's author believe that every `Smiley` should be able to blink? Explain.

> The author believes that every 'Smiley' should be able to blink, as the blinkable function can interface with smiley and simply enabled within the main executable.
>

2. For those smileys that blink, does the author expect them to blink in the same way? Explain.

> The author expects them to blink the same way, as the paramaters been specifically defined to blink once with a delay of 0.25 seconds.
>

3. Referring to the implementation of blink in the Happy and Sad Smiley classes, give a brief explanation of what polymorphism is.

> Polymorphism is an objected-oriented programming concept that allows different classes to define methods with the same name, but modifying its behaviour specific to each class. For example both happy and sad smiley can use the blinkable property, but you can set the happy to blink momentarily, whilst the sad one can be set by dimming or altering its sad expression.
>

4. How is inheritance used in the blink method, and why is it important for polymorphism?

> Inheritance is important for polymorphism because it establishes a relationship between classes that allows them to be treated as instances of the same parent type.
>
1. **Implement Blink in Sad Class:**

   - Create a new method called `blink` within the Sad class. Ensure you use the same method signature as in the Happy class:

   ```python
   def blink(self, delay=0.25):
       pass  # Replace 'pass' with your implementation
   ```

2. **Code Implementation:** Implement the code that allows the Sad smiley to blink. Use the implementation from the Happy Smiley as a reference. Ensure your new method functions similarly by controlling the blink duration through the `delay` argument.

3. **Testing the Implementation:**

- Test the new blink functionality on your Raspberry Pi or within the Python classes provided. You might need to adjust the `main.py` script to incorporate Sad Smiley's new blinking capability.

Include a screenshot of the sad smiley or the modified `main.py`:

<img width="667" height="469" alt="image" src="https://github.com/user-attachments/assets/85b0b2c0-f014-4647-99c4-74f330a9a8fe" />

- Observe and document the Sad smiley as it blinks its eyes. Describe any adjustments or issues encountered during implementation.

  > The only adjustments i made was to swap the happy part in smiley = Happy() to smiley = sad. Otherwise had no issues occurred during implementation.

  ### 2.8. If It Walks Like a Duck…

  Previously, you implemented the blink functionality for the Sad smiley without utilizing the class `Blinkable`. Assuming you did not use `Blinkable` (even if you actually did), consider how the Sad smiley could blink similarly to the Happy smiley without this specific class.

  1. **Class Type Analysis:** What kind of class is `Blinkable`? Inspect its superclass for clues about its classification.

     > Blinkable is an abstract class

  2. **Class Implementation:** `Blinkable` is a class intended to be implemented by other classes. What generic term describes this kind of class, which is designed for implementation by others? **Clue**: Notice the lack of any concrete implementation and the naming convention.

  > The generic term for a class that is intended to be implemented by other class, would be an abstract class, or sometimes also referred to as an interface.

  3. **OO Principle Identification:** Regarding your answer to question (2), which Object-Oriented (OO) principle does this represent? Choose from the following and justify your answer in 1-2 sentences: Abstraction, Polymorphism, Inheritance, Encapsulation.

  > Abstraction is the object-oriented principle that is represented by the class Blinkable. That is because Blinkable defines the idea of an object that can blink without specifying how the blink works, with the details of its implementation hidden.

  4. **Implementation Flexibility:** Explain why you could grant the Sad Smiley a blinking feature similar to the Happy Smiley's implementation, even without directly using `Blinkable`.

  > By writing a blink() method for the Sad subclass. Even without implementing the interface, any class can define a method with the same name and behaviour as another class. As long as the blink() method exists, it can still perform blinking functionality.

  5. **Concept and Language Specificity:** In relation to your response to question (4), what is this capability known as, and why is it feasible in Python and many other dynamically typed languages but not in most statically typed programming languages like C#? **Clue** This concept is hinted at in the title of this section.

  > This capability is known as duck typing. In dynamically typed languages like Python, an object does not need to formally implement an interface like Blinkable to use a method such as blink() whereas in contrast, statically typed languages like C# require classes to explicitly implement an interface or inherit from a base class to be considered valid for a certain behaviour.

  ***

  ## 3. Refactoring

  ### 3.1. Does a Smiley Have to Be Yellow?

  While our current implementation predominantly features yellow smileys, emotional expressions like sickness or anger typically utilize colors like green, red, or orange. We'll explore the feasibility of integrating these colors into our smileys.

  1. **Defined Colors and Their Location:**

     1. Which colors are defined and in which class(s)?
        > Only the Smiley class has the colors defined, and it has white, green, yellow and red colors.
     2. What type of variables hold these colors? Are the values expected to change during the program's execution? Explain your answer.
        > They are not expected to change during execution, because they represent fixed color definitions that all smileys use consistently. Their purpose is to provide reusable values for rendering different expressions, not to store dynamic data.
     3. Add the color blue to the appropriate class using the appropriate format and values.
        <img width="401" height="158" alt="image" src="https://github.com/user-attachments/assets/8d6a4f8f-957d-44a1-bca0-be84686d4afd" />


  2. **Usage of Color Variables:**

     1. In which classes are the color variables used?
        > The color variables defined in the Smiley class are used by its subclasses, such as Happy or Sad, or in any future defined subclass that inherits the properties of Smiley.

  3. **Simple Method to Change Colors:**
  4. What is the easiest way you can think to change the smileys to green? Easiest, not necessarily the best!
     > By directly changing the color values in the Smiley class where the colors are defined.



  ### 3.2. Flexible Colors – Step 1

  Changing the color of the smileys once is straightforward, but it isn't very flexible. To facilitate various colors for smileys, it is advisable not to hardcode values in any class. This approach was identified earlier as a necessary change. Let's start by removing the built-in assumptions about color in our classes.

  1. **Add a method called `complexion` to the `Smiley` class:** Implement this instance method to return `self.YELLOW`. Using the term "complexion" instead of "color" provides a more abstract terminology that focuses on the meaning rather than implementation.
  <img width="645" height="415" alt="image" src="https://github.com/user-attachments/assets/727ba6c9-cc0a-48f4-9694-4f8779f4d5f4" />

  2. **Refactor subclasses to use the `complexion` method:** Modify any subclass that directly accesses the color variable to instead utilize the new `complexion` method. This ensures that color handling is centralized and can be easily modified in the future.
  <img width="501" height="261" alt="image" src="https://github.com/user-attachments/assets/a1024e64-505e-49f6-8c2c-4aa0f18af3c7" />

  3. **Determine the applicable Object-Oriented principle:** Consider whether Abstraction, Polymorphism, Inheritance, or Encapsulation best applies to the modifications made in this step.
  > The modifications made in this step best represent Abstraction. By introducing the complexion() method, we moved colour handling away from specific implementations and into a more general, meaningful concept. Instead of directly accessing self.YELLOW, subclasses now rely on an abstract idea of a “complexion.” This hides the implementation detail of how the colour is stored and focuses instead on what it represents.

  4. **Verify the implementation:** Ensure that the modifications function as expected. The smileys should still display in yellow, confirming that the new method correctly replaces the direct color references.
  > The smiley is still yellow after these modifications.

  This step is crucial for setting up a more flexible system for color management in the smiley display logic, allowing for easy adjustments and extensions in the future.

  ### 3.3. Flexible Colors – Step 2

  Having removed the hardcoded color values, we now enhance the base class to support dynamic color assignments more effectively.

  1. **Modify the `__init__()` method in the `Smiley` class:** Introduce a default argument named `complexion` and assign `YELLOW` as its default value. This allows the instantiation of smileys with customizable colors.
  <img width="729" height="480" alt="image" src="https://github.com/user-attachments/assets/4cf5f8ac-059b-4ce1-9f78-9ad470d90d19" />

  2. **Introduce a new instance variable:** Create a variable called `my_complexion` and assign the `complexion` parameter to it. This step ensures that each smiley instance can maintain its own color state.
  <img width="712" height="407" alt="image" src="https://github.com/user-attachments/assets/4a0c56d1-bf7f-40f9-ad35-3c26c233f5b7" />

  3. **Rationale for `my_complexion`:** Using a distinct instance variable like `my_complexion` avoids potential conflicts with the method parameter names and clarifies that it is an attribute specific to the object.

  4. **Bulk rename:** We want to update our grid to use the value of complexion, but we have so many `Y`'s in the grid. Use your IDE's refactoring tool to rename all instances of the **symbol** `Y` to `X`. Where `X` is the value of the `complexion` variable. Include a screenshot evidencing you have found the correct refactor tool and the changes made.
  <img width="550" height="551" alt="image" src="https://github.com/user-attachments/assets/050c211d-736b-4732-b021-0cc1c8cf56dc" />
  <img width="238" height="227" alt="image" src="https://github.com/user-attachments/assets/9003ec2d-f2e4-4120-abc1-153f8f618bea" />

  5. **Update the `complexion` method:** Adjust this method to return `self.my_complexion`, ensuring that whatever color is assigned during instantiation is what the smiley displays.

  6. **Verification:** Run the updated code to confirm that Smileys still defaults to yellow unless specified otherwise.

  ### 3.4. Flexible Colors – Step 3

  With the foundational changes in place, it's now possible to implement varied smiley colors for different emotional expressions.

  1. **Adjust the `Sad` class initialization:** In the `Sad` class's initializer method, change the superclass call to include the `complexion` argument with the value `self.BLUE`, as shown:

     ```python
     super().__init__(complexion=self.BLUE)
     ```

  2. **Test color functionality for the Sad smiley:** Execute the program to verify that the Sad smiley now appears blue.

  3. **Ensure the Happy smiley remains yellow:** Confirm that changes to the Sad smiley do not affect the default color of the Happy smiley, which should still display in yellow.

  4. **Design and Implement An Angry Smiley:** Create an Angry smiley class that inherits from the `Smiley` class. Set the color of the Angry smiley to red by passing `self.RED` as the `complexion` argument in the superclass call.

  ***
