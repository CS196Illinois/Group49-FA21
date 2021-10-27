/*
import React, { useRef, useEffect, useState } from 'react';
import { BrowserRouter, NavLink, Switch, Route, useLocation } from 'react-router-dom';
import companyLogo from './public/team.png';
import FileUpload from "./components/file-upload/file-upload.component";
import './App.css';

function App() {

  const navbarLinks = useRef(null);
  const handleNavbarButton = (e) => {
    navbarLinks.current.classList.toggle('menu-collapse');
  };

  const hideNavMenu = () => {
    if (!navbarLinks.current.classList.contains('menu-collapse')) {
      navbarLinks.current.classList.add('menu-collapse');
    }
  };

  const [newUserInfo, setNewUserInfo] = useState({
    profileImages: []
  });

  
  const updateUploadedFiles = (files) =>
    setNewUserInfo({ ...newUserInfo, profileImages: files });

  const handleSubmit = (event) => {
    event.preventDefault();
  };

  return (
    <div className="App">
      <BrowserRouter>
        <nav className='navbar'>
          <div className='navbar-container'>
            <a href="#" className='brand-title'>Group-49</a>
            <button onClick={(e) => { handleNavbarButton(e); }} className='navbar-toggler'>
              <span className='navbar-toggler-icon'></span>
            </button>
            <div ref={navbarLinks} className='navbar-links menu-collapse'>
              <ul className='links-list'>
                <li className='nav-item'>
                  <NavLink activeClassName='is-active' exact={true} className='nav-link' to='/'>Home</NavLink>
                </li>
                <li className='nav-item'>
                  <NavLink activeClassName='is-active' exact={true} className='nav-link' to='/about'>About</NavLink>
                </li>
                <li className='nav-item'>
                  <NavLink activeClassName='is-active' exact={true} className='nav-link' to='/team'>Team</NavLink>
                </li>
              </ul>
            </div>
          </div>
        </nav>

      
        <div className='container'>
          <AllRoutes hideMenu={() => { hideNavMenu(); }}></AllRoutes>
        </div>

        <div>
      <form onSubmit={handleSubmit}>
        <FileUpload
          accept=".jpg,.png,.jpeg"
          label="Profile Image(s)"
          multiple
          updateFilesCb={updateUploadedFiles}
        />
        <button type="submit">Create New User</button>
      </form>
    </div>
      </BrowserRouter>
    </div>
  );
}

function AllRoutes({ hideMenu }) {

  let location = useLocation();
  useEffect(() => {
    hideMenu();
  }, [location]);

  return (
    <Switch>
      <Route path="/about" component={About}>
      </Route>
      <Route path="/team" component={Team}>
      </Route>
      <Route path="/" component={Home}>
      </Route>
    </Switch>
  );
}



function Home() {
  return (
    <div>
      <h1>Home page</h1>
      <img src={companyLogo} alt="BigCo Inc. logo" height = {500} width = {500} className="center"/>
      
    </div>
  );
}

function About() {
  return (
    <h1>About Page</h1>
  );
}

function Team() {
  return (
    <h1>Team</h1>
  );
}
export default App;
*/
import React, { useRef, useEffect, useState } from 'react';
import { BrowserRouter, NavLink, Switch, Route, useLocation } from 'react-router-dom';
import companyLogo from './public/team.png';
import FileUpload from "./components/file-upload/file-upload.component";
import './App.css';

function App() {

  const navbarLinks = useRef(null);
  const handleNavbarButton = (e) => {
    navbarLinks.current.classList.toggle('menu-collapse');
  };

  const hideNavMenu = () => {
    if (!navbarLinks.current.classList.contains('menu-collapse')) {
      navbarLinks.current.classList.add('menu-collapse');
    }
  };

  const [newUserInfo, setNewUserInfo] = useState({
    profileImages: []
  });

  const updateUploadedFiles = (files) =>
    setNewUserInfo({ ...newUserInfo, profileImages: files });

  const handleSubmit = (event) => {
    event.preventDefault();
    //logic to create new user...
  };

  return (
    <div className="App">
      <BrowserRouter>
        <nav className='navbar'>
          <div className='navbar-container'>
            <a href="#" className='brand-title'>Group-49</a>
            <button onClick={(e) => { handleNavbarButton(e); }} className='navbar-toggler'>
              <span className='navbar-toggler-icon'></span>
            </button>
            <div ref={navbarLinks} className='navbar-links menu-collapse'>
              <ul className='links-list'>
                <li className='nav-item'>
                  <NavLink activeClassName='is-active' exact={true} className='nav-link' to='/'>Home</NavLink>
                </li>
                <li className='nav-item'>
                  <NavLink activeClassName='is-active' exact={true} className='nav-link' to='/about'>About</NavLink>
                </li>
                <li className='nav-item'>
                  <NavLink activeClassName='is-active' exact={true} className='nav-link' to='/team'>Team</NavLink>
                </li>
              </ul>
            </div>
          </div>
        </nav>
        
      
        <div className='container'>
          <AllRoutes hideMenu={() => { hideNavMenu(); }}></AllRoutes>
        </div>

    <div>
      <form onSubmit={handleSubmit}>
        <FileUpload
          accept=".jpg,.png,.jpeg"
          label="Profile Image(s)"
          multiple
          updateFilesCb={updateUploadedFiles}
        />
        <button type="submit">Create New User</button>
      </form>
    </div>
    </BrowserRouter>
    </div>
  );
}

function AllRoutes({ hideMenu }) {

  let location = useLocation();
  useEffect(() => {
    hideMenu();
  }, [location]);

  return (
    <Switch>
      <Route path="/about" component={About}>
      </Route>
      <Route path="/team" component={Team}>
      </Route>
      <Route path="/" component={Home}>
      </Route>
    </Switch>
  );
}



function Home() {
  return (
    <div>
      <h1>Home page</h1>
      <img src={companyLogo} alt="BigCo Inc. logo" height = {500} width = {500} className="center"/>
      
    </div>
  );
}

function About() {
  return (
    <h1>About Page</h1>
  );
}

function Team() {
  return (
    <h1>Team</h1>
  );
}

export default App;