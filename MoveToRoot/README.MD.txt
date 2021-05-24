This is a batch script that apon cloning to a root parent folder, clones and removes any adjacent files in children folders.

Before script
Root
|-MoveToRoot.bat
|__Child1
   |-Child1_sub1.txt
   |-Child1_sub2.txt
|__Child2
   |-Child2_sub1.txt
   |-Child2_sub2.txt

After
Root
|-MoveToRoot.bat
|-Child1_sub1.txt
|-Child1_sub2.txt
|-Child2_sub1.txt
|-Child2_sub2.txt
|__Child1
|__Child2