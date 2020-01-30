# FST_structure
I found interesting algorithm what I heard from UCDAVIS friend. while staying in USA.
so, I'm studying FST_data structure
FST, it can be used in AI technology area.
such as a NLP ( Natural Language Processing )
I want to share with you guys. if you don't know it.

------------------------------
 - Finite state Transducers

![Image 4](https://github.com/LeeGitaek/FST_structure/blob/master/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202020-01-30%20%E1%84%8B%E1%85%A9%E1%84%8C%E1%85%A5%E1%86%AB%2010.10.31.png?raw=true)


K = Finite set of states
Σ = Alphabet of INPUT
Γ = Alphabet of OUTPUT
s = s ∈ K = Start State
F c k = Accept States
Δ = Relation From
    K x (Σ U ∈) to K x (Γ U ∈) 

![Image 5](https://github.com/LeeGitaek/FST_structure/blob/master/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202020-01-30%20%E1%84%8B%E1%85%A9%E1%84%8C%E1%85%A5%E1%86%AB%2010.15.06.png?raw=true)


K = { 0 , 1 } 
Σ = { a , b }
Σ U ∈ = { a , b , ∈ } 

K x (Σ U ∈) = { <0, a>, <0, b>,<0, ∈>,
                <1, a>, <1, b>,<1, ∈> }
                
Γ = { x , y , z } 
Γ U ∈ = { x , y , z , ∈ }

K x (Γ U ∈) = { <<0, a>, <0, x>>,
                <<0, b>, <0, y>>,
                <<0, a>, <1, z>>}
                
Therefore it would be "xyyz" ,if input is "abba".
FST has a stack-based interface.     

I will add more information after study FST.



ref) https://web.stanford.edu/~laurik/publications/pmatch.pdf
This is from Stanford. if you need more information. 
