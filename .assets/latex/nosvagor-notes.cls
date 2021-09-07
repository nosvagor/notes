% ███╗   ██╗ ██████╗ ████████╗███████╗███████╗
% ████╗  ██║██╔═══██╗╚══██╔══╝██╔════╝██╔════╝
% ██╔██╗ ██║██║   ██║   ██║   █████╗  ███████╗
% ██║╚██╗██║██║   ██║   ██║   ██╔══╝  ╚════██║
% ██║ ╚████║╚██████╔╝   ██║   ███████╗███████║
% ╚═╝  ╚═══╝ ╚═════╝    ╚═╝   ╚══════╝╚══════╝
%  →-.   →  .-'.   →  .--.   →  .--.   →  .--.   →  .-→
% →::.\::::::::.\::::::::.\::::::::.\::::::::.\:::::::→→ → 
% → →:.\:::: https://github.com/nosvagor/notes \:::→→ →  →  → 
% →::::.\::::::::.\::::::::.\::::::::.\::::::::.\::::→  →
%   → →   `--'  →   `.-'  →   `--'  →   `--'  →   `--' →  → 

\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{nosvagor-notes}[2021/08/01 Multipurpose hierarchical structured notes]
\LoadClass[12pt,a4paper]{report}

% ╔═╗┌─┐┌─┐┌─┐
% ╠═╝├─┤│ ┬├┤ 
% ╩  ┴ ┴└─┘└─┘
\RequirePackage[hmargin=2.4cm, vmargin=2cm, headsep=1.3em]{geometry} 
    \raggedright 
    \setlength\headheight{16pt}
    \setlength{\parskip}{1ex plus 2ex minus 0ex}
    \renewcommand{\baselinestretch}{1.2} 
\RequirePackage[parfill]{parskip}

% ╔═╗┌─┐┌─┐┌┬┐┬┌─┐┌┐┌┌─┐
% ╚═╗├┤ │   │ ││ ││││└─┐
% ╚═╝└─┘└─┘ ┴ ┴└─┘┘└┘└─┘
\RequirePackage{titlesec}
\RequirePackage[object=vectorian]{pgfornament}
    \titleformat{\chapter}
    {\LARGE\centering\bfseries\color{title-color}}
    {}{0pt}{}[
    \vspace{-16pt}\hspace{2pt}
    {\hyperlink{ToC}{\pgfornament[width=8cm,ydelta=10pt]{84}}}
    \vspace{-2pt}
    ]
        
    \titlespacing*{\chapter}{0pt}{-78pt}{0pt} 
    
    \newcommand{\sectionbreak}{\clearpage}
    
    \titleformat{\section}
    {\Large\bfseries\color{sec}}
    {}{0pt}{}

    \titlespacing*{\section}{0pt}
        {1ex plus 7ex minus 1ex}
        {1ex plus 0ex minus 0ex}

    \titleformat{\subsection}{\large\bfseries\color{ssec}}
    {}{0pt}{}
    
    \titlespacing*{\subsection}{0pt}
        {1ex plus 6.9ex minus 1ex}
        {1ex plus 6.9ex minus 0ex}

% ╔═╗┌─┐┌┐┌┌┬┐┌─┐┌┐┌┌┬┐┌─┐
% ║  │ ││││ │ ├┤ │││ │ └─┐
% ╚═╝└─┘┘└┘ ┴ └─┘┘└┘ ┴ └─┘
\RequirePackage{titletoc}
    \renewcommand{\contentsname}{\color{title-color}\theTitle}
    \setcounter{tocdepth}{2}
    \titlecontents{chapter}[0 em]
        {\vspace{12pt}\large\bfseries\color{title-color}}{}{}
        {\hfill}[\vspace{-3pt}]
    \titlecontents{section}[0.809 em]
        {\vspace{3pt}\bfseries}{}{}
        {\hfill\contentspage}
    \titlecontents{subsection}[1.618 em]
        {\color{minor}}{}{}
        {\titlerule*[0.42 em]{.}\contentspage}
    
%  ╦  ┬┌─┐┌┬┐┌─┐
%  ║  │└─┐ │ └─┐
%  ╩═╝┴└─┘ ┴ └─┘
\RequirePackage{enumitem}
    \setlist[itemize,enumerate]{itemsep=-0.3ex,topsep=-0.3ex,partopsep=-0.3ex,leftmargin=\dimexpr1em}

    \setlist[itemize,1]{label=\small\(\color{minor}\bullet\)}
    \setlist[itemize,2]{label=\small\(\circ\)}
    \setlist[itemize,3]{label=\small\color{minor}\textbullet,}

    \setlist[enumerate]{leftmargin=\dimexpr1.5em}

% ╔═╗┌─┐┌┐┌┌┬┐┌─┐
% ╠╣ │ ││││ │ └─┐
% ╚  └─┘┘└┘ ┴ └─┘
\RequirePackage[T1]{fontenc}
\RequirePackage{cmbright}
    \SetSymbolFont{largesymbols}{normal}{OMX}{iwona}{m}{n}
    \SetSymbolFont{largesymbols}{bold}{OMX}{iwona}{b}{n}
\RequirePackage[sfdefault, light]{roboto}

% ╦ ╦┌─┐┌─┐┌┬┐┌─┐┬─┐   ┬   ╔═╗┌─┐┌─┐┌┬┐┌─┐┬─┐
% ╠═╣├┤ ├─┤ ││├┤ ├┬┘  ┌┼─  ╠╣ │ ││ │ │ ├┤ ├┬┘
% ╩ ╩└─┘┴ ┴─┴┘└─┘┴└─  └┘   ╚  └─┘└─┘ ┴ └─┘┴└─
\RequirePackage{fancyhdr}
    \pagestyle{fancy}
    \fancyhead{}
        \renewcommand{\chaptermark}[1]{\markboth{#1}{}}
        \renewcommand{\sectionmark}[1]{\markright{#1}{}}

    \fancyhead[L]{
        \hyperlink{ToC}{{\color{title-color}\nouppercase\leftmark}}}
    \fancyhead[R]{
        \hyperlink{ToC}{{\color{sec}\nouppercase\rightmark}}
        }
    \cfoot{
        {\color{title-color}\hyperlink{ToC}{
        \pgfornament[width=0.42cm,ydelta=-4pt]{11}
        \hspace{-4pt}\thepage
        \hspace{2pt}\pgfornament[width=0.42cm,ydelta=-4pt]{14}
    }}}

    \fancypagestyle{plain}{
    \fancyhead{}
        \renewcommand{\headrulewidth}{0pt}
    \cfoot{
        {\color{title-color}\hyperlink{ToC}{
        \pgfornament[width=0.42cm,ydelta=-4pt]{11}
        \hspace{-4pt}\thepage
        \hspace{2pt}\pgfornament[width=0.42cm,ydelta=-4pt]{14}
    }}}
    }

% ╦ ╦┌┬┐┬┬  ┬┌┬┐┬ ┬
% ║ ║ │ ││  │ │ └┬┘
% ╚═╝ ┴ ┴┴─┘┴ ┴  ┴ 
\RequirePackage[hidelinks]{hyperref}
    \hypersetup{
        colorlinks=false,
        linktoc=all,    
        linkcolor=ggg,
        filecolor=ggg,      
        urlcolor=ggg, 
    }

\RequirePackage{graphicx, booktabs, multirow, multicol, makecell, xcolor, pagecolor, changepage, apacite,pifont,fontawesome}

\RequirePackage[justification=centering]{caption}
    \captionsetup[table]{
        skip=3pt,
        labelformat=empty,
    }
    \AtBeginDocument{
        \let\oldcaption\caption
        \renewcommand{\caption}[1]{\oldcaption{\ssec{\textbf{#1}}}}
    }
    \newcommand{\mc}[1]{\makecell[c]{#1}}
    \newcommand{\mr}[1]{\makecell[r]{#1}}

\RequirePackage{siunitx}
    \sisetup{
        inter-unit-product = \ensuremath{{\cdot}},
}


% ╔═╗┌─┐┌┬┐┌┬┐┌─┐┌┐┌┌┬┐┌─┐
% ║  │ │││││││├─┤│││ ││└─┐
% ╚═╝└─┘┴ ┴┴ ┴┴ ┴┘└┘─┴┘└─┘
\newcommand{\chonk}[1]{{\Large{\textbf{#1}}}}
\newcommand{\pts}[1]{\textbf{[ \hspace{16pt} / #1 ]}}

\newcommand{\Image}[2]{
    \raisebox{-.5\height}{\includegraphics[width=#1]{#2}}
}
\newcommand{\Arrow}{
    \raisebox{-.5\height}{\scalebox{2}{\(~\rightarrow~\)}}
}

\newcommand{\qqquad}{\hspace{3em}}

\def\ipt{\hspace{1pt}}
\def\iipt{\hspace{2pt}}


%  ██████╗ ██████╗ ██╗      ██████╗ ██████╗ ███████╗
% ██╔════╝██╔═══██╗██║     ██╔═══██╗██╔══██╗██╔════╝
% ██║     ██║   ██║██║     ██║   ██║██████╔╝███████╗
% ██║     ██║   ██║██║     ██║   ██║██╔══██╗╚════██║
% ╚██████╗╚██████╔╝███████╗╚██████╔╝██║  ██║███████║
%  ╚═════╝ ╚═════╝ ╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝
% ╔╗ ┌─┐┌─┐┌─┐
% ╠╩╗├─┤└─┐├┤ 
% ╚═╝┴ ┴└─┘└─┘
% Background: #1f1f1f #141414 
\definecolor{bg}{HTML}{1f1f1f} 
    \newcommand{\bg}[1]{{\color{bg}#1}}
    \pagecolor{bg} % Background Color
\definecolor{dark}{HTML}{141414}
    \newcommand{\dark}[1]{{\color{dark}#1}}

% Text: #ebebeb #e0e0e0 #b0b0b0 #949494 #6b6b6b #404040 
\definecolor{bright}{HTML}{ebebeb}  
    \newcommand{\bright}[1]{{\color{bright}#1}}
\definecolor{fg}{HTML}{e0e0e0}  
    \newcommand{\fg}[1]{{\color{fg}#1}}
    \color{fg} % Foreground Color
\definecolor{prn}{HTML}{b0b0b0}
    \newcommand{\prn}[1]{{\color{prn}(#1)}}
\definecolor{minor}{HTML}{949494} 
    \newcommand{\minor}[1]{{\color{minor}#1}}
\definecolor{minimal}{HTML}{6b6b6b} 
    \newcommand{\minimal}[1]{{\color{minimal}#1}}
\definecolor{faint}{HTML}{404040} 
    \newcommand{\faint}[1]{{\color{faint}#1}} 

% Emphasis: #f5af71 #f5984c #f58ecc #4ca9f5
\definecolor{ooo}{HTML}{f5af71} 
    \newcommand{\ooo}[1]{{\color{ooo}#1}} 
    % \let\oldemph\emph
    \renewcommand{\emph}[1]{{\color{ooo}#1}}
\definecolor{OOO}{HTML}{f5984c} 
    \newcommand{\OOO}[1]{{\color{OOO}#1}}
\definecolor{ppp}{HTML}{f5769c}
    \newcommand{\ppp}[1]{{\color{ppp}#1}}
\definecolor{bBb}{HTML}{4ca9f5}
    \newcommand{\bBb}[1]{{\color{bBb}#1}}


% Sections: #7abef5 #b0d0eb #cedeeb
\definecolor{sec}{HTML}{7abef5} 
    \newcommand{\tsec}[1]{{\color{sec}{#1}}}
    \newcommand{\Tsec}[1]{{\color{sec}{\textbf{#1}}}}
\definecolor{ssec}{HTML}{b0d0eb} 
    \newcommand{\ssec}[1]{{\color{ssec}{#1}}}
    \newcommand{\Ssec}[1]{{\color{ssec}{\textbf{#1}}}}
\definecolor{ddd}{HTML}{cedeeb} 
    \newcommand{\ddD}[1]{{\color{ddd}{#1}}}
    \newcommand{\ddd}[1]{{\color{ddd}{\textbf{#1}}}}
    

% Links: #81de84 #66b06b
\definecolor{ggg}{HTML}{81de84}
    \newcommand{\src}[1]{{\vspace{-6pt}\color{ggg}{{\footnotesize\faGlobe}}\,}{\small{#1}}}
    \newcommand{\link}[2]{
        \href{#1}{\color{ggg}{{#2}\small\(\,^\text{\faChain}\)}}
    }
    \newcommand{\linky}[2]{
        \href{#1}{\color{ggg}{{#2}\small\(\,^\text{\,\faYoutubePlay}\)}}
    }
\definecolor{GGG}{HTML}{66b06b}
    \newcommand{\GGG}[1]{{\color{GGG}{#1}}}
    \newcommand{\ulink}[1]{\GGG{{#1}\small\(\,^\uparrow\)}}
    \newcommand{\dlink}[1]{\GGG{{#1}\small\(\,^\downarrow\)}}
    

% ╔╦╗┬┌─┐┬ ┬┌─┐┌┬┐┌─┐┌┬┐┬ ┬
%  ║║││  ├─┤│ │ │ │ ││││└┬┘
% ═╩╝┴└─┘┴ ┴└─┘ ┴ └─┘┴ ┴ ┴ 
% Charge: #678ff5#2560f5 → #f57067#f53325
\definecolor{rrr}{HTML}{f57067}
    \newcommand{\RRR}[1]{{\color{RRR}{#1}}}
\definecolor{RRR}{HTML}{f53325}
    \newcommand{\rrr}[1]{{\color{rrr}{#1}}}
\definecolor{bbb}{HTML}{678ff5}
    \newcommand{\bbb}[1]{{\color{bbb}{#1}}}
\definecolor{BBB}{HTML}{2560f5}
    \newcommand{\BBB}[1]{{\color{BBB}{#1}}}

% Boolean: #4cf5d9 → #f54c7f
\definecolor{ttt}{HTML}{57d9c3}
    \newcommand{\ttt}[1]{{\color{ttt}{#1}}}
    \newcommand{\cmark}{\ding{51}}
    \newcommand{\true}[1]{\ttt{\cmark~#1}}

\definecolor{fff}{HTML}{f54c7f}
    \newcommand{\fff}[1]{{\color{fff}{#1}}}
    \newcommand{\xmark}{\ding{56}\,}
    \newcommand{\false}[1]{\fff{\xmark~#1}}

% Relative: #c88ef5#ac4cf5 → #f5e48e#f5d94c
\definecolor{xxx}{HTML}{c88ef5}  
    \newcommand{\xxx}[1]{{\color{xxx}{#1}}}
\definecolor{XXX}{HTML}{ac4cf5}  
    \newcommand{\XXX}[1]{{\color{XXX}{#1}}}
\definecolor{yyy}{HTML}{f5e48e}  
    \newcommand{\yyy}[1]{{\color{yyy}{#1}}}
\definecolor{YYY}{HTML}{f5d94c}  
    \newcommand{\YYY}[1]{{\color{YYY}{#1}}}

%                  ╦═╗┌─┐┌─┐┌─┐┬─┐┌─┐┌┐┌┌─┐┌─┐
%                  ╠╦╝├┤ ├┤ ├┤ ├┬┘├┤ ││││  ├┤ 
%                  ╩╚═└─┘└  └─┘┴└─└─┘┘└┘└─┘└─┘

%                 fff #f54c7f       #f53325 RRR
%            ppp #f5769c                 #f57067 rrr
%                          ____________              
%                         /\  ________ \         
%      xxx #c88ef5       /  \ \______/\ \        #f5af71  emph
%    XXX #ac4cf5        / /\ \ \  / /\ \ \         #f5984c str
%                      / / /\ \ \/ / /\ \ \
%                     / / /__\_\/ / /__\_\ \
%   BBB #2560f5      / /_/_______/ /________\       
%    bbb #678ff5     \ \ \______ \ \______  /   
%                     \ \ \  / /\ \ \  / / /        #f5e48e yyy
%                      \ \ \/ / /\ \ \/ / /       #f5d94c YYY
%       bBb #4ca9f5     \ \/ / /__\_\/ / /         
%                        \  / /______\/ /
%      sec #7abef5        \/___________/
%    ssec #b0d0eb                              #81de84 ggg
%  ddd  #cedeeb                             #66b06b GGG
%                         #4cf5d9 ttt      
%                                             
%  #ebebeb bight                     
%    /\ 
%   /  \ #e0e0e0 foreground (fg)
%  / /\ \ 
%  \ \/ / 
%   \ \/ #b0b0b0 parens
%   /\ \ 
%   \ \/ #949494 minor
%   /\ \ 
%   \ \/ #808080 
%   /\ \ 
%  / /\ \ #6b6b6b minimal
%  \ \ \/ 
%  /\ \ \
%  \ \/ / #4f4f4f
%   \ \/
%   /\ \ #404040 faint
%   \ \/
%   /\ \ #2f2f2f 
%   \ \/
%   /\ \ #262626
%  / /\ \
%  \ \/ / 
%   \  / #1f1f1f background (bg)
%    \/                      
%  #141414 dark

% ╔═╗┌─┐┌┬┐┬┌─┐┌┐┌┌─┐
% ║ ║├─┘ │ ││ ││││└─┐
% ╚═╝┴   ┴ ┴└─┘┘└┘└─┘
\DeclareOption{light}{
    \pagecolor{white}
    \color{black}

    \titleformat{\chapter}{\LARGE\bfseries}{}{0pt}{\centering}
    \titleformat{\section}{\Large\bfseries}{}{0pt}{}
    \titleformat{\subsection}{\large\bfseries}{}{0pt}{}
    \titleformat{\subsubsection}{\large\bfseries}{}{0pt}{} 

    \hypersetup{colorlinks,linkcolor={BBB},citecolor={BBB},urlcolor={BBB}} 
}

\DeclareOption{basic}{
    \pagestyle{fancy}
    \lhead{\userName}
    \chead{\textsc{\theTitle}}
    \rhead{\today}    
    \cfoot{\textsc{\institution}}
    \rfoot{\thepage}
    \lfoot{\class}
}

\ProcessOptions\relax