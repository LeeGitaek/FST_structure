# FST_structure
I found interesting algorithm what I heard from UCDAVIS friend. while staying in USA.
so, I'm studying FST_data structure.
FST, it can be used in AI technology area.
such as a NLP ( Natural Language Processing )
I want to share with you guys. if you don't know it.

------------------------------
 - Finite state Transducers

![Image 4](https://github.com/LeeGitaek/FST_structure/blob/master/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202020-01-30%20%E1%84%8B%E1%85%A9%E1%84%8C%E1%85%A5%E1%86%AB%2010.10.31.png?raw=true)


K = Finite set of states <br>
Σ = Alphabet of INPUT<br>
Γ = Alphabet of OUTPUT<br>
s = s ∈ K = Start State<br>
F c k = Accept States<br>
Δ = Relation From
    K x (Σ U ∈) to K x (Γ U ∈) 
<br>
![Image 5](https://github.com/LeeGitaek/FST_structure/blob/master/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202020-01-30%20%E1%84%8B%E1%85%A9%E1%84%8C%E1%85%A5%E1%86%AB%2010.15.06.png?raw=true)


K = { 0 , 1 } <br>
Σ = { a , b }<br>
Σ U ∈ = { a , b , ∈ } <br>

K x (Σ U ∈) = { <0, a>, <0, b>,<0, ∈>,
                <1, a>, <1, b>,<1, ∈> }
                <br>
Γ = { x , y , z } <br>
Γ U ∈ = { x , y , z , ∈ }<br>

K x (Γ U ∈) = { <<0, a>, <0, x>>,
                <<0, b>, <0, y>>,
                <<0, a>, <1, z>>}
                <br>
Therefore it would be "xyyz" ,if input is "abba".
FST has a stack-based interface.     
<br>
I will add more information after study FST.

<br>

ref) https://web.stanford.edu/~laurik/publications/pmatch.pdf<br>
This is from Stanford. if you need more information. 
