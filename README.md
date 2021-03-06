[![Build Status](https://travis-ci.com/ebranlard/welib.svg?branch=master)](https://travis-ci.com/ebranlard/welib)
<a href="https://www.buymeacoffee.com/hTpOQGl" rel="nofollow"><img alt="Donate just a small amount, buy me a coffee!" src="https://warehouse-camo.cmh1.psfhosted.org/1c939ba1227996b87bb03cf029c14821eab9ad91/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f446f6e6174652d4275792532306d6525323061253230636f666665652d79656c6c6f77677265656e2e737667"></a>

# welib

Suite of python and matlab tools for aero-servo-hydro-elasticity (aerodynanmics, controls, hydrodynamics, structure/elasticity) and wind energy.

# Examples of application

Aerodynamic applications:

- Manipulation of airfoil curves, find slopes, interpolate (see `welib\airfoils\examples\`)
- Run different dynamic stall models (e.g Oye or Morten Hansen) (see `welib\airfoils\examples\`)

Structural dynamics and system dynamics applications:

- Setup the equation of motions for a multibody system with flexible members analytically or numerically (see `welib\yams\examples`)
- Linearize a non-linear system defined by a state and output equation (implicit or explicit) (see `welib\system\tests\`
- Perform 2d/3d FEM analyses using beam/frame elements (see 'welib\FEM')
- Craig-Bampton / Guyan reduction of a structure (see 'welib\FEM')
- Perform time integration of mechanical systems (see `welib\system\examples`)


Controls applications:

- Run a kalman filter to estimate states of a system (see `welib\kalman\`)



Wind energy applications:

- Run steady state BEM simulations (see `welib\BEM\examples\`)
- Read and write common wind energy file formats (see `welib\weio`, a clone of [weio](http://github.com/ebranlard/weio/))
- Generate stochastic wind and waves times series
- Estimate wind speed (see 'welib\ws\_estimator`))

Other:

-  Spectral analyses, signal processing, time integration, vector analyses


See also:

- [pyDatView](http://github.com/ebranlard/pyDatView/): GUI to visualize files (supported by weio) and perform analyses on the data


# Installation and testing
```bash
git clone http://github.com/ebranlard/welib
cd welib
python -m pip install -r requirements.txt
python -m pip install -e .
pytest
```


# Libraries

The repository contains a set of small packages, for aerodynamics, structure, control and more:

- airfoils: polar manipulations, dynamic stall models
- beams: analytical results for beams
- BEM: steady and unsteady bem code
- ctrl: control tools
- dyninflow: dynamic inflow models
- fastlib: tools to handle OpenFAST models (run simulations, postprocess, linear model)
- FEM: Finite Element Method tools (beams)
- kalman: kalman filter
- mesh: meshing tools
- ode: tools for time integration of ODE
- standards: some formulae and scripts useful for the IEC standards
- system: tools for dynamic systems (e.g. LTI, state space) and mechanical systems (M,C,K matrices), eigenvalue analysis, time integration
- tools: mathematical tools, signal processing
- weio: library to read and write files used in wind energy, clone of [weio](http://github.com/ebranlard/weio/) 
- wt\_theory: scripts implementing some wind turbine aerodynamic theory 
- ws\_estimator: wind speed estimator for wind energy based on tabulated Cp Ct
- yams: multibody analyses




# Contributing
Any contributions to this project are welcome! If you find this project useful, you can also buy me a coffee (donate a small amount) with the link below:


<a href="https://www.buymeacoffee.com/hTpOQGl" rel="nofollow"><img alt="Donate just a small amount, buy me a coffee!" src="https://warehouse-camo.cmh1.psfhosted.org/1c939ba1227996b87bb03cf029c14821eab9ad91/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f446f6e6174652d4275792532306d6525323061253230636f666665652d79656c6c6f77677265656e2e737667"></a>
