// Goal
// Over the centuries a language evolves, and not only do words appear or disappear, but some letters become more used or on the contrary less used.

// In order to be able to quickly analyze many texts, we want to develop a program that calculates how many times a given letter is present in a text.
// Input
// Line 1: A character C that will be searched for
// Line 2: An integer N
// Next N lines: a string with length len
// Output
// the number of times that C appears in the text
// Constraints
// 0 ≤ len ≤ 1000
// Example
// Input
// E
// 2
// JE VOUS REMECTZ A LA GRANDE CHRONICQUE PANTAGRUELINE 
// RECONGNOISTRE LA GENEALOGIE ET ANTIQUITE DONT NOUS EST VENU GARGANTUA
// Output
// 16

C=readline();N=+readline();c=0;for(i=0;i<N;c+=readline().split(C).length-1,i++);console.log(c);

r=readline;C=r();N=+r();c=0;for(i=0;i<N;c+=r().split(C).length-1,i++);console.log(c);