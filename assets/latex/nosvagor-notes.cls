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
\ProvidesClass{nosvagor-notes}[2021/09/08 functional notes,]
\LoadClass[12pt,a4paper]{report}
\RequirePackage{nosvagor-commands}

% ╔═╗┌─┐┌─┐┌─┐
% ╠═╝├─┤│ ┬├┤
% ╩  ┴ ┴└─┘└─┘
\RequirePackage[hmargin=2.4cm, vmargin=1.1cm, headsep=0pt]{geometry}
  \raggedright
  \setlength\headheight{0pt}
  \setlength{\parskip}{1ex plus 2ex minus 0ex}
  \renewcommand{\baselinestretch}{1.2}
  \RequirePackage[parfill]{parskip}

% ╔═╗┌─┐┌─┐┌┬┐┬┌─┐┌┐┌┌─┐
% ╚═╗├┤ │   │ ││ ││││└─┐
% ╚═╝└─┘└─┘ ┴ ┴└─┘┘└┘└─┘
\RequirePackage{titlesec}
\RequirePackage[object=vectorian]{pgfornament}
  \titleformat{\chapter}
  {\LARGE\centering\bfseries\scshape\color{title-color}}
  {}{0pt}{}[
  \vspace{-6pt}\hspace*{1pt}
    {\hyperlink{ToC}{\pgfornament[width=8cm]{84}}}
  ]

  \titlespacing*{\chapter}{0pt}{-36pt}{0pt}

  \newcommand{\sectionbreak}{\clearpage}

  \titleformat{\section}
  {\Large\bfseries\color{primary}}
  {}{0pt}{}

  \titlespacing*{\section}
  {0pt}
  {1ex plus 7ex minus 1ex}
  {1ex plus 0ex minus 0ex}

  \titleformat{\subsection}
  {\large\bfseries\color{primary-1}}
  {}{0pt}{}

  \titlespacing*{\subsection}
  {0pt}
  {1ex plus 6.9ex minus 1ex}
  {1ex plus 6.9ex minus 0ex}

% ╔═╗┌─┐┌┐┌┌┬┐┌─┐┌┐┌┌┬┐┌─┐
% ║  │ ││││ │ ├┤ │││ │ └─┐
% ╚═╝└─┘┘└┘ ┴ └─┘┘└┘ ┴ └─┘
\RequirePackage{titletoc}
\renewcommand{\contentsname}{\color{title-color}\hspace{2pt}\theTitle}

  \setcounter{tocdepth}{2}

  \titlecontents{chapter}[0 em]
  {\vspace{12pt}\large\bfseries\scshape\color{title-color}}
  {}{}
  {\hfill}[\vspace{-3pt}]

  \titlecontents{section}[0.809 em]
  {\vspace{3pt}\bfseries}
  {}{}
  {\hfill\contentspage}

  \titlecontents{subsection}[1.618 em]
  {\color{foreground-2}}
  {}{}
  {\titlerule*[0.42 em]{.}\contentspage}

%  ╦  ┬┌─┐┌┬┐┌─┐
%  ║  │└─┐ │ └─┐
%  ╩═╝┴└─┘ ┴ └─┘
\RequirePackage{enumitem}
  \setlist[itemize,enumerate]{itemsep=-0.3ex,topsep=-0.3ex,partopsep=-0.3ex,leftmargin=\dimexpr1em}

  \setlist[itemize,1]{label=\raisebox{1pt}{\small\color{primary}\(\bullet\)}}
  \setlist[itemize,2]{label=\raisebox{1pt}{\small\color{primary-1}\(\circ\)}}
  \setlist[itemize,3]{label=\small{\color{primary-2}\textbullet}}

  \setlist[enumerate]{leftmargin=\dimexpr1em}

% ╔═╗┌─┐┌┐┌┌┬┐┌─┐
% ╠╣ │ ││││ │ └─┐
% ╚  └─┘┘└┘ ┴ └─┘
\RequirePackage[T1]{fontenc}
\RequirePackage{cmbright}
  \SetSymbolFont{largesymbols}{normal}{OMX}{iwona}{m}{n}
  \SetSymbolFont{largesymbols}{bold}{OMX}{iwona}{b}{n}
  \RequirePackage[sfdefault, light]{roboto}

% ╔═╗┌─┐┌─┐┌┬┐┌─┐┬─┐
% ╠╣ │ ││ │ │ ├┤ ├┬┘
% ╚  └─┘└─┘ ┴ └─┘┴└─
\RequirePackage{fancyhdr}
  \pagestyle{fancy}{
  \fancyhf{}
  \renewcommand{\headrulewidth}{0pt}
  \cfoot{\hspace{4pt}
    {
      \color{title-color}\hyperlink{ToC}{
        \pgfornament[width=0.42cm,ydelta=-4pt]{11}
        \hspace{-3pt}\thepage
        \hspace{3pt}\pgfornament[width=0.42cm,ydelta=-4pt]{14}
      }
    }
  }

  \fancypagestyle{plain}{
    \fancyhf{}
    \renewcommand{\headrulewidth}{0pt}
    \cfoot{\hspace{4pt}
      {
        \color{title-color}\hyperlink{ToC}{
          \pgfornament[width=0.42cm,ydelta=-4pt]{11}
          \hspace{-3pt}\thepage
          \hspace{3pt}\pgfornament[width=0.42cm,ydelta=-4pt]{14}
        }
      }
    }
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

\RequirePackage{
  graphicx, booktabs, multirow, multicol, xcolor, pagecolor,
  changepage, apacite, pifont, fontawesome5, fontawesome
}

\RequirePackage[justification=centering]{caption}
  \captionsetup{
    % skip=-15pt,
    labelformat=empty,
  }


  \RequirePackage{siunitx}
  \sisetup{
    % inter-unit-product = \ensuremath{{\cdot}},
  }


% ╦┌┐┌┬┌─┌─┐┌─┐┌─┐┌─┐┌─┐
% ║│││├┴┐└─┐│  ├─┤├─┘├┤
% ╩┘└┘┴ ┴└─┘└─┘┴ ┴┴  └─┘

\RequirePackage{import, pdfpages, transparent}
  \pdfsuppresswarningpagegroup=1

  \newcommand{\incfig}[2][1]{%
    \def\svgwidth{#1\columnwidth}
    \import{./figures/}{#2.pdf_tex}
  }

% ╔╦╗┌─┐┌─┐╔╗ ┌─┐┌─┐┬┌┐┌
%  ║║│ ││  ╠╩╗├┤ │ ┬││││
% ═╩╝└─┘└─┘╚═╝└─┘└─┘┴┘└┘

\AtBeginDocument{
  \let\oldcaption\caption
  \renewcommand{\caption}[1]{\oldcaption{{\color{primary-1}{\textbf{#1}}}}}

  \hypertarget{ToC}{\tableofcontents}

  \let\oldchapter\chapter
  \renewcommand{\chapter}[1]{
    \oldchapter{#1}\label{c:#1}
  }
  \let\oldsection\section
  \renewcommand{\section}[1]{
    \oldsection{#1}\label{s:#1}
  }
  \let\oldsubsection\subsection
  \renewcommand{\subsection}[1]{
    \oldsubsection{#1}\label{ss:#1}
  }
}

%  ██████╗ ██████╗ ██╗      ██████╗ ██████╗ ███████╗
% ██╔════╝██╔═══██╗██║     ██╔═══██╗██╔══██╗██╔════╝
% ██║     ██║   ██║██║     ██║   ██║██████╔╝███████╗
% ██║     ██║   ██║██║     ██║   ██║██╔══██╗╚════██║
% ╚██████╗╚██████╔╝███████╗╚██████╔╝██║  ██║███████║
%  ╚═════╝ ╚═════╝ ╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝

% Base
\definecolor{foreground-3}{HTML}{484e6b}
\definecolor{foreground-2}{HTML}{7b839e}
\definecolor{foreground-1}{HTML}{a2a5ba}
\definecolor{foreground}{HTML}{c6c8d1}
\definecolor{foreground+1}{HTML}{e9ebf5}

\definecolor{background-1}{HTML}{010103}
\definecolor{background}{HTML}{161821}
\definecolor{background+1}{HTML}{292e47}

\definecolor{primary-2}{HTML}{cedeeb}
\definecolor{primary-1}{HTML}{b0d0eb}
\definecolor{primary}{HTML}{7abef5}

% Colors
\definecolor{red}{HTML}{e36866}
\definecolor{red+1}{HTML}{fa4441}

\definecolor{orange}{HTML}{e39866}
\definecolor{orange+1}{HTML}{fa8b41}

\definecolor{yellow}{HTML}{e3d178}
\definecolor{yellow+1}{HTML}{f5d94c}

\definecolor{green}{HTML}{95cf78}
\definecolor{green+1}{HTML}{84f54c}

\definecolor{cyan}{HTML}{7bd4b8}
\definecolor{cyan+1}{HTML}{41fadb}

\definecolor{blue}{HTML}{6685e3}
\definecolor{blue+1}{HTML}{4271ff}

\definecolor{magenta}{HTML}{a376b8}
\definecolor{magenta+1}{HTML}{bb5fe3}

\definecolor{pink}{HTML}{e278ad}
\definecolor{pink+1}{HTML}{f54088}

% Lets
\pagecolor{background}
\color{foreground}

\definecolor{accent}{HTML}{f5b37a}
\definecolor{accent-alt}{HTML}{f57ab1}

\colorlet{link-internal}{green}
\colorlet{link-external}{cyan}

% ╔═╗┌─┐┌┬┐┬┌─┐┌┐┌┌─┐
% ║ ║├─┘ │ ││ ││││└─┐
% ╚═╝┴   ┴ ┴└─┘┘└┘└─┘
\DeclareOption{assignment}{
  \pagestyle{fancy}
  \lhead{\userName}
  \chead{\textsc{\theTitle}}
  \rhead{\today}
  \cfoot{\textsc{\institution}}
  \rfoot{\thepage}
  \lfoot{\class}
}


\DeclareOption{basic} {

\renewcommand{\RRR}[1]{{\color{red}{#1}}}
\renewcommand{\RR}[1]{{\color{red+1}{#1}}}

\renewcommand{\OOO}[1]{{\color{orange}{#1}}}
\renewcommand{\OO}[1]{{\color{orange+1}{#1}}}

\renewcommand{\YYY}[1]{{\color{yellow}{#1}}}
\renewcommand{\YY}[1]{{\color{yellow+1}{#1}}}

\renewcommand{\GGG}[1]{{\color{green}{#1}}}
\renewcommand{\GG}[1]{{\color{green+1}{#1}}}

\renewcommand{\CCC}[1]{{\color{cyan}{#1}}}
\renewcommand{\CC}[1]{{\color{cyan+1}{#1}}}

\renewcommand{\BBB}[1]{{\color{blue}{#1}}}
\renewcommand{\BB}[1]{{\color{blue+1}{#1}}}

\renewcommand{\MMM}[1]{{\color{magenta}{#1}}}
\renewcommand{\MM}[1]{{\color{magenta+1}{#1}}}

\renewcommand{\PPP}[1]{{\color{pink}{#1}}}
\renewcommand{\PP}[1]{{\color{pink+1}{#1}}}

\pagecolor{white}
\color{black}

\renewcommand{\contentsname}{\color{title-color}\hspace{2pt}\theTitle\vspace{-12pt}}

\definecolor{darkblue}{HTML}{1d2c6d}
\renewcommand{\dd}[1]{{\color{darkblue}{\textbf{#1}}}}
\renewcommand{\2}[1]{{\color{darkblue}{#1}}}

\titleformat{\chapter}
{\LARGE\centering\bfseries\scshape\color{title-color}}{}{0pt}{}[]

\titlecontents{subsection}[1.618 em]
{\color{black!80!white}\itshape}
{}{}
{\titlerule*[0.42 em]{.}\contentspage}

\titlecontents{section}[0.809 em]
{\vspace{3pt}}
{}{}
{\hfill\contentspage}

\titlecontents{chapter}[0 em]
{\vspace{12pt}\large\bfseries\scshape\color{title-color}}
{}{}
{\hfill}[\vspace{-3pt}]


\titleformat{\section}
{\Large\bfseries\color{darkblue!42!black}}
{}{0pt}{}

\titleformat{\subsection}
{\vspace{16pt}\large\bfseries\itshape\color{darkblue!69!black}}
{}{0pt}{}


\setlist[itemize,1]{label=\raisebox{1pt}{\small\(\bullet\)}}
\setlist[itemize,2]{label=\raisebox{1pt}{\small\(\circ\)}}
\setlist[itemize,3]{label=\small{\textbullet}}

}

\ProcessOptions\relax
