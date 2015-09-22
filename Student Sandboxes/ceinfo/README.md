# ApplicationSecurity
For our application security course - repository <BR>
This is for assignment 1, the Turing machine.  <BR>

<B>To make and run this program:</B> <BR>
&nbsp; &nbsp; 1)  Place all files and place into a local directory (ex: "/u/ceinfo/test"). <BR>
&nbsp; &nbsp; 2)  Make sure the .java, .dat, and makefile are located in the same directory (ex: "/u/ceinfo/test"). <BR>
&nbsp; &nbsp; 3)  Run:  "cd /u/ceinfo/test" <BR>
&nbsp; &nbsp; 4)  Run:  "./makefile" <BR>
&nbsp; &nbsp; 5)  The makefile automatically compiles the main java program,  then executes the fibonacci program, then executes the powersOfTwo program, then executes the addSub program.  <BR><BR>


<B>To run the program once the code is compiled:</B> <BR>
&nbsp; &nbsp; 1) Run:  "java TuringTest <inputfile>"  (ex:  "java TuringTest fibonacci.dat") <BR><BR>

<B>Details on creating a dat file:</B>  <BR>
&nbsp;&nbsp; 1.	The operations and file formats for each operation are as follows:
<BR>&nbsp;&nbsp;&nbsp;&nbsp;a.	SET – allows the user to set the index of the position in an ArrayList with a value;  formatted as “SET,<position>,<value>”.  <BR>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;i.	For example, “SET,1,23” will set the value of 23 into array[1].
<BR>&nbsp;&nbsp;&nbsp;&nbsp;b.	ADD – allows the user to add two positions in memory and place the final sum into the index of the third position;  formatted as “ADD,<firstPosition>,<secondPosition>,<thirdPosition> “.
<BR>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; i.	For example, “ADD,1,2,3” will set array[3] = array[1] + array[2].
<BR>&nbsp;&nbsp;&nbsp;&nbsp;c.	SUB – allows the user to subtrace two positions in memory and place the final subtracted value into the index of the third position;  formatted as “SUB,<firstPosition>,<secondPosition>,<thirdPosition> “.
<BR>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;i.	For example, “SUB,1,2,3” will set array[3] = array[1] - array[2].
<BR>&nbsp;&nbsp;&nbsp;&nbsp;d.	MUL – allows the user to multiply two positions in memory and place the multiplied value into the index of the third position;  formatted as “MUL,<firstPosition>,>,<secondPosition>,<thirdPosition> “.
<BR>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; i.	For example, “MUL,1,2,3” will set array[3] = array[1] * array[2].
<BR>&nbsp;&nbsp;&nbsp;&nbsp;e.	DISP - allows the user to display the value in the index of the firstPosition;  formatted as “DISPL,<firstPosition>”.
<BR>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;i.	For example, “DISPL,1”  will print array[1];
<BR>&nbsp;&nbsp;&nbsp;&nbsp;f.	HALT - allows the user to halt the program gracefully.
<BR>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;i.	For example, “HALT” will simply end the program.



Thanks!<BR>
CE<BR>

