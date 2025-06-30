<div align="center">

<a target="_blank" title="Picked off of Google Images"><img width="196px" alt="gowebly logo" src="https://static.vecteezy.com/system/resources/previews/007/547/493/non_2x/cosine-graph-line-icon-vector.jpg"></a>

<a name="readme-top"></a>

# Turing Engine α
A fun little math engine akin to a Computer Algebra System (CAS). 
<br></br>
Version Alpha. Created this this repo on Turing's Birthday.
</div>

# Some Math I need to keep in mind while building this
## Axioms
**Axiom 2.1:** 0 is a natural number.
<br/>---<br/>
**Axiom 2.2:** If $n$ is a natural number, then $n++$ is also a natural number.
<br/>---<br/>
**Axiom 2.3:** 0 is not the successor of any natural number; i.e., we have $n++ \neq 0$ for every natural number $n$.
<br/><br/>
_Remark on Axiom 2.3:_ This axiom is to prevent a wrap around natural number set. For example, $\{0, 1, 2, 3\}$ can justified as a natural number system as $n++$ from 3 can be wrapped to 0.
<br/>---<br/>
**Axiom 2.4:** Different natural numbers must have different successors; i.e., if $n, m$ are natural numbers and $n \neq m$, then $n++ \neq m++$. Equivalently, if $n++ = m++$ then we must have $n = m$.
<br/>---<br/>
**Axiom 2.5:** (_Principle of Mathematical Induction)_ Let $P(n) be any property pertaining to a natural number $n$. Suppose that $P(0)$ is true, and suppose that whenever $P(n)$ is true, $P(n++)$ is also true. Then $P(n)$ is true for every natural number $n$. 
<br/><br/>
_Remark on Axiom 2.5:_ This axiom serves as a template to make sequences. This tool makes streams of entities and proves them correct. Very useful for when trying to create a series of entities that hold one true property across the board.
<br/><br/>


