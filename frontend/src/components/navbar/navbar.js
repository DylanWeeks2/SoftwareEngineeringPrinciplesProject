import React, { useState } from 'react';
import {
  Collapse,
  Navbar,
  NavbarToggler,
  NavbarBrand,
  Nav,
  NavItem,
  NavLink,
} from 'reactstrap';

const Example = (props) => {
  const [isOpen, setIsOpen] = useState(false);

  const toggle = () => setIsOpen(!isOpen);

  return (
    <div>
      <Navbar color="dark" dark expand="md">
        <NavbarBrand href="/managerView">Tantrum Sunless Tanning Scheduler</NavbarBrand>
        <NavbarToggler onClick={toggle} />
        <Collapse isOpen={isOpen} navbar>
          <Nav className="ml-auto" navbar>
          <NavItem>
              <NavLink href="/managerView">Home</NavLink>
            </NavItem>
            <NavItem>
              <NavLink href="/employee">Employees</NavLink>
            </NavItem>
            <NavItem>
              <NavLink href="/location">Locations</NavLink>
            </NavItem>
            <NavItem>
              <NavLink href="/calendar">Calendar</NavLink>
            </NavItem>
            <NavItem>
              <NavLink href="/past-schedules">Past Schedules</NavLink>
            </NavItem>
            <NavItem>
              <NavLink href="/requests">Request Days Off</NavLink>
            </NavItem>
            <NavItem>
              <NavLink href="/logout">Logout</NavLink>
            </NavItem>
          </Nav>
        </Collapse>
      </Navbar>
    </div>
  );
}

export default Example;