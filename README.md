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

<br>
 * Example of FSTs *  <br>

The action of a Finite State Transducer can be viewed as computing a relation between two sets.<br>
It defines a relation between two sets of strings.<br>

 ** This is from Stackoverflow ** <br>

<br>
For input 11 you start (as always) in state 0. <br>
The transition labeled 1/0 takes you to state 1, reads the first 1 from the input and outputs 0.<br>

![Image 8](https://github.com/LeeGitaek/FST_structure/blob/master/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202020-01-30%20%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE%204.47.36.png?raw=true)


#1. Now there is one 1 of your input left , so you take 1/1 to state 0. <br>
#2. The first step outputs 0, the second one 1 , so the total output is 01.<br>
#3. x:y means that the transition reads x and outputs y.<br>

ref ) https://cs.nyu.edu/~mohri/postscript/csl01.pdf

[ FST ] KOREAN
유한상태 변환기 <br>
튜링기계의 용어에 따라 입력 테이프와 출력 테이프라는 두개의 메모리 테이프가 있는 유한 상태 기계이다. <br>
두 set의 symbol 사이를 매핑하는 유한상태 오토마톤유형이다. <br>

- 한국어 형태소 분석기 (FST기반) , 2016년 최초 <br>
- 검색 시스템에 사용될 수 있으며 , AI NLP 에도 이용될 수 있다. <br>

** FINITE STATE COMPUTING ** < br>

LATER <br>

WEIGHTED FINITE STATE TRANSDUCER <br>
 
![Image 5](https://github.com/LeeGitaek/FST_structure/blob/master/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202020-01-31%20%E1%84%8B%E1%85%A9%E1%84%8C%E1%85%A5%E1%86%AB%2011.06.54.png?raw=true)
 <br>

FST 는 분석의 INPUT / OUTPUT symbol pair를 바꾸기만 하면 '생성 모델' 이 된다. <br>
장점 :<br>

    1) High level information 넣는 것이 수월하다.<br>
    
    2) 수학적으로 sound 하다.<br>
    
    3) 실행속도가 빠르다.
    
![Image 5](https://github.com/LeeGitaek/FST_structure/blob/master/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202020-01-30%20%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE%203.56.36.png?raw=true) <br>   

    
단점 :<br>

    1) 절대 시간 이상의 공부가 필요하다. <br>
    
   
UCDavis Document <br>

ref ) https://web.cs.ucdavis.edu/~rogaway/classes/120/spring13/eric-transducers.pdf <br>




