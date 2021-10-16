import React from 'react'
import {Container, Nav, Navbar} from "react-bootstrap";
import {Link} from "react-router-dom";
import {DataContext} from "../../contexts/DataContext";


const MenuExampleProps = () => {
    const {data} = React.useContext(DataContext)
    const [expanded, setExpanded] = React.useState(false);

    return (
        <Navbar bg="dark" variant="dark" expand="sm" expanded={expanded}>
            <Container>
                <Navbar.Brand as={Link} to="/">{data && <>{data.first_name + " " + data.last_name}</>}</Navbar.Brand>
                <Navbar.Toggle aria-controls="basic-navbar-nav"
                               onClick={() => setExpanded(expanded ? false : "expanded")}/>
                <Navbar.Collapse id="basic-navbar-nav">
                    <Nav className="me-auto">
                        <Nav.Link as={Link} to="/me" onClick={() => setExpanded(false)}>About me</Nav.Link>
                        <Nav.Link as={Link} to="/work" onClick={() => setExpanded(false)}>Work</Nav.Link>
                        <Nav.Link as={Link} to="/hobby" onClick={() => setExpanded(false)}>Hobbies</Nav.Link>
                        <Nav.Link as={Link} to="/contact" onClick={() => setExpanded(false)}>Contact</Nav.Link>
                    </Nav>
                </Navbar.Collapse>
            </Container>
        </Navbar>
    )
}

export default MenuExampleProps
