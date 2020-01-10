\NeedsTeXFormat{LaTeX2e}[1994/06/01]
\ProvidesClass{kuee_en}[English Latex Template used in KUEE]

% Packages
\RequirePackage{lipsum}
\RequirePackage{xcolor,graphicx,tikz,pgfplots}

\RequirePackage{physics}
\RequirePackage[version=4]{mhchem} % chemical formula, \ce{H2O}
\RequirePackage{siunitx} % SI units

\RequirePackage{CJKutf8}
\newcommand*{\cjk}[1]{%
  \begin{CJK}{UTF8}{ipxm}#1\end{CJK}
}

% set lengths
\setlength{\topmargin}{0mm} 
\setlength{\headheight}{12pt} 
\setlength{\headsep}{25pt} 
\setlength{\footskip}{30pt} 
\setlength{\oddsidemargin}{0.5cm} 
\setlength{\evensidemargin}{0.5cm} 
\setlength{\textwidth}{424pt}
\setlength{\textheight}{604pt}
\setlength{\marginparwidth} {68pt}

\LoadClass[12pt,a4paper]{report}

\newcommand*{\supervisor}[1]{\gdef\@supervisor{#1}}
\newcommand*{\@supervisor}{\texttt{\string\supervisor} currently not set. Please fix this.}
\newcommand*{\school}[1]{\gdef\@school{#1}}
\newcommand*{\@school}{\texttt{\string\school} currently not set. Please fix this.}
\newcommand*{\depart}[1]{\gdef\@depart{#1}}
\newcommand*{\@depart}{\texttt{\string\depart} currently not set. Please fix this.}
\newcommand*{\eauthor}[1]{\gdef\@eauthor{#1}}
\newcommand*{\etitle}[1]{\gdef\@etitle{#1}}

% title set
\renewcommand{\maketitle}{%
\begin{titlepage}
	\centering
      \unitlength = 1cm
      \begin{picture}(0,0)(0.5,10)
        \put(2.5,8){\makebox(0,0)[b]{\makebox[8cm]{\Huge \cjk{修\hfil士\hfil論\hfil文}}}}%
        \put(-2.5,5.5){\makebox(0,0)[r]{\makebox[2cm]{\cjk{題\hfil 目}}}}%
        \put(2.5,5.5){\makebox(0,0){\parbox{10cm}{\center \LARGE \@title}}}%
        \put(-2.5,3){\makebox(0,0)[r]{\makebox[2cm]{\cjk{指\hfil 導\hfil 教\hfil 員}}}}%
        \put(2.5,3){\makebox(0,0){\parbox{8cm}{\center \LARGE \@supervisor}}}%
        \put(2.5,-6.5){\makebox(0,0)[t]{\@school\ \@depart}}%
        \put(-0.5,-8.5){\makebox(0,0)[rb]{\makebox[1.5cm]{\cjk{氏\hfil 名}}}}%
        \put(2.5,-8.7){\makebox(0,0)[b]{\LARGE \underline{\@author}}}%
        \put(2.5,-10){\makebox(0,0)[t]{\large \@date}}%
      \end{picture}
    \hfill\let\maketitle\relax
\end{titlepage}   
}

% abstract page same as japanese version
\renewcommand*{\abstractname}{
    {\Large\bfseries\@etitle}
  \begin{flushright}
    \@eauthor
  \end{flushright}
  \begin{flushleft}
    {\bfseries Abstract}
  \end{flushleft}%
}

% custom contents 
\renewcommand{\tableofcontents}{%
\bgroup
\def\thepage{\roman{page}}%
\lineskip = \normallineskip
\@restonecolfalse
\if@twocolumn\@restonecoltrue\onecolumn\fi
\chapter*{\contentsname\@mkboth{\contentsname}{\contentsname}}%
\@starttoc{toc}
\if@restonecol\twocolumn\fi
\newpage
\egroup
\setcounter{page}{1}
}

% ackpage
\newenvironment{acknowledgements}{%
    \chapter*{Acknowledgements}
    \addcontentsline{toc}{chapter}{Acknowledgements}
}{%
}

% \renewcommand{\bibname}{References}

\endinput