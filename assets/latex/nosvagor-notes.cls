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
  {\LARGE\centering\bfseries\color{title-color}}
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
  {\vspace{12pt}\large\bfseries\color{title-color}}
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

  \setlist[itemize,1]{label=\small{\color{primary}\(\bullet\)}}
  \setlist[itemize,2]{label=\small{\color{primary-1}\(\circ\)}}
  \setlist[itemize,3]{label=\small{\color{primary-2}\textbullet}}

  \setlist[enumerate]{leftmargin=\dimexpr1.5em}

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
  changepage, apacite, pifont, fontawesome,
}

% NOTE: why do I have this?
\RequirePackage[justification=centering]{caption}
  \captionsetup[table]{
    skip=3pt,
    labelformat=empty,
  }

  \AtBeginDocument{
    \let\oldcaption\caption
    \renewcommand{\caption}[1]{\oldcaption{\ssec{\textbf{#1}}}}

    % TODO: get the sections-labels into here?

  }

  \RequirePackage{siunitx}
  \sisetup{
    inter-unit-product = \ensuremath{{\cdot}},
  }


%  ██████╗ ██████╗ ██╗      ██████╗ ██████╗ ███████╗
% ██╔════╝██╔═══██╗██║     ██╔═══██╗██╔══██╗██╔════╝
% ██║     ██║   ██║██║     ██║   ██║██████╔╝███████╗
% ██║     ██║   ██║██║     ██║   ██║██╔══██╗╚════██║
% ╚██████╗╚██████╔╝███████╗╚██████╔╝██║  ██║███████║
%  ╚═════╝ ╚═════╝ ╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝


% Base
\definecolor{foreground-3}{HTML}{}
\definecolor{foreground-2}{HTML}{818596}
\definecolor{foreground-1}{HTML}{}
\definecolor{foreground}{HTML}{c6c8d1}
\definecolor{foreground+1}{HTML}{}

\definecolor{background-1}{HTML}{}
\definecolor{background}{HTML}{161821}
\definecolor{background+1}{HTML}{}

\definecolor{primary-2}{HTML}{cedeeb}
\definecolor{primary-1}{HTML}{b0d0eb}
\definecolor{primary}{HTML}{7abef5}

\colorlet{accent-1}{orange+2}
\colorlet{accent}{orange}
\colorlet{accent+1}{orange+1}

\colorlet{link-internal}{green-1}
\colorlet{link-external}{green}


% Colors
\definecolor{red-1}{HTML}{}
\definecolor{red}{HTML}{e27878}
\definecolor{red+1}{HTML}{}

\definecolor{orange-1}{HTML}{}
\definecolor{orange}{HTML}{e2a478}
\definecolor{orange+1}{HTML}{}

\definecolor{yellow-1}{HTML}{}
\definecolor{yellow}{HTML}{e2d078}
\definecolor{yellow+1}{HTML}{}

\definecolor{green-1}{HTML}{}
\definecolor{green}{HTML}{b4be82}
\definecolor{green+1}{HTML}{}

\definecolor{cyan-1}{HTML}{}
\definecolor{cyan}{HTML}{89b8c2}
\definecolor{cyan+1}{HTML}{}

\definecolor{blue-1}{HTML}{}
\definecolor{blue}{HTML}{84a0c6}
\definecolor{blue+1}{HTML}{}

\definecolor{puprle-1}{HTML}{}
\definecolor{purple}{HTML}{a093c7}
\definecolor{purple+1}{HTML}{}

\definecolor{pink-1}{HTML}{}
\definecolor{pink}{HTML}{e278ad}
\definecolor{pink+1}{HTML}{}

%

\pagecolor{background}
\color{foreground}


% ╔═╗┌─┐┌┬┐┬┌─┐┌┐┌┌─┐
% ║ ║├─┘ │ ││ ││││└─┐
% ╚═╝┴   ┴ ┴└─┘┘└┘└─┘
% \DeclareOption{light}{
%   \pagecolor{white}
%   \color{black}

%   \titleformat{\chapter}{\LARGE\bfseries}{}{0pt}{\centering}
%   \titleformat{\section}{\Large\bfseries}{}{0pt}{}
%   \titleformat{\subsection}{\large\bfseries}{}{0pt}{}
%   \titleformat{\subsubsection}{\large\bfseries}{}{0pt}{}

%   \hypersetup{colorlinks,linkcolor={BBB},citecolor={BBB},urlcolor={BBB}}
% }

% \DeclareOption{basic}{
%   \pagestyle{fancy}
%   \lhead{\userName}
%   \chead{\textsc{\theTitle}}
%   \rhead{\today}
%   \cfoot{\textsc{\institution}}
%   \rfoot{\thepage}
%   \lfoot{\class}
% }

\DeclareOption{light}{
% Base
\definecolor{foreground-3}{HTML}{}
\definecolor{foreground-2}{HTML}{}
\definecolor{foreground-1}{HTML}{}
\definecolor{foreground}{HTML}{}
\definecolor{foreground+1}{HTML}{}

\definecolor{background-1}{HTML}{}
\definecolor{background}{HTML}{}
\definecolor{background+1}{HTML}{}
\definecolor{background+2}{HTML}{}
\definecolor{background+3}{HTML}{}

\definecolor{primary-3}{HTML}{}
\definecolor{primary-2}{HTML}{}
\definecolor{primary-1}{HTML}{}
\definecolor{primary}{HTML}{}

\definecolor{accent-1}{HTML}{}
\definecolor{accent}{HTML}{}
\definecolor{accent+1}{HTML}{}

\definecolor{link-internal}{HTML}{}
\definecolor{link-external}{HTML}{}

% Colors
\definecolor{red}{HTML}{}
\definecolor{red+1}{HTML}{}

\definecolor{orange}{HTML}{}
\definecolor{orange+1}{HTML}{}

\definecolor{yellow}{HTML}{}
\definecolor{yellow+1}{HTML}{}

\definecolor{green}{HTML}{}
\definecolor{green+1}{HTML}{}

\definecolor{cyan}{HTML}{}
\definecolor{cyan+1}{HTML}{}

\definecolor{blue}{HTML}{}
\definecolor{blue+1}{HTML}{}

\definecolor{purple}{HTML}{}
\definecolor{purple+1}{HTML}{}

\definecolor{pink}{HTML}{}
\definecolor{pink+1}{HTML}{}
}

%%%%

\DeclareOption{dark}{
% Base
\definecolor{foreground-3}{HTML}{}
\definecolor{foreground-2}{HTML}{}
\definecolor{foreground-1}{HTML}{}
\definecolor{foreground}{HTML}{}
\definecolor{foreground+1}{HTML}{}

\definecolor{background-1}{HTML}{}
\definecolor{background}{HTML}{}
\definecolor{background+1}{HTML}{}
\definecolor{background+2}{HTML}{}
\definecolor{background+3}{HTML}{}

\definecolor{primary-3}{HTML}{}
\definecolor{primary-2}{HTML}{}
\definecolor{primary-1}{HTML}{}
\definecolor{primary}{HTML}{}

\definecolor{accent-1}{HTML}{}
\definecolor{accent}{HTML}{}
\definecolor{accent+1}{HTML}{}

\definecolor{link-internal}{HTML}{}
\definecolor{link-external}{HTML}{}

% Colors
\definecolor{red}{HTML}{}
\definecolor{red+1}{HTML}{}

\definecolor{orange}{HTML}{}
\definecolor{orange+1}{HTML}{}

\definecolor{yellow}{HTML}{}
\definecolor{yellow+1}{HTML}{}

\definecolor{green}{HTML}{}
\definecolor{green+1}{HTML}{}

\definecolor{cyan}{HTML}{}
\definecolor{cyan+1}{HTML}{}

\definecolor{blue}{HTML}{}
\definecolor{blue+1}{HTML}{}

\definecolor{purple}{HTML}{}
\definecolor{purple+1}{HTML}{}

\definecolor{pink}{HTML}{}
\definecolor{pink+1}{HTML}{}
}

\ProcessOptions\relax
