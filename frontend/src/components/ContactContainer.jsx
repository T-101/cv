import React from 'react'
import {Card, Col, Row, Table} from "react-bootstrap";
import {DataContext} from "../contexts/DataContext";
import lol_decrypt from "../services/utils";
import FAIcon from "./FAIcon";


export default function LandingPageContainer() {
    const {data} = React.useContext(DataContext)
    const buttonStylesSmall = {
        width: "1.5em",
        fontSize: "1.5em"
    }
    const buttonStyles = {
        width: "1.5em",
        fontSize: "2.5em"
    }
    if (data) {
        document.title = "CV | Contact | " + data.first_name + " " + data.last_name
    }
    return (
        <Row xs={1} lg={2}>
            <Col style={{marginTop: "30px"}}>
                <Card>
                    <Card.Header>Contact</Card.Header>
                    <Card.Body>
                        <Table>
                            <tbody>
                            {data && data.emails.map((value, key) => (
                                <tr key={key}>
                                    <td>
                                        <FAIcon icon={"fas fa-at"} {...buttonStylesSmall}/>
                                        <a href={"mailto:" + lol_decrypt(value.address)}>{lol_decrypt(value.address)}</a>
                                    </td>
                                </tr>
                            ))}
                            {data && data.phone_numbers.map((value, key) => (
                                <tr key={key}>
                                    <td>
                                        <FAIcon icon={value.fa_class} {...buttonStylesSmall}/>
                                        <a href={"tel:" + lol_decrypt(value.number).replace(/-/g, "")}>{lol_decrypt(value.number)}</a>
                                    </td>
                                </tr>
                            ))}
                            {data && data.external_links.map((value, key) => (
                                <tr key={key}>
                                    <td>
                                        <a href={value.url}><FAIcon
                                            icon={value.fa_class} {...buttonStyles}/> {value.title}</a>
                                    </td>
                                </tr>
                            ))}
                            </tbody>
                        </Table>
                    </Card.Body>
                </Card>
            </Col>
            <Col style={{marginTop: "30px"}}>
                <Card>
                    <Card.Header>CV Tech Info</Card.Header>
                    <Card.Body>
                        <Table>
                            <tbody>
                            <tr>
                                <td>
                                    Backend
                                </td>
                                <td>
                                    <a href="https://docs.python.org/3.9/">Python 3.9.7</a><br/>
                                    <a href="https://docs.djangoproject.com/en/3.2/">Django 3.2.7</a><br/>
                                    <a href="https://www.django-rest-framework.org/">Django Rest Framework 3.12.4</a>
                                </td>
                            </tr>
                            <tr>
                                <td>
                                    Frontend
                                </td>
                                <td>
                                    <a href="https://reactjs.org/">ReactJS 17.0.2</a>
                                </td>
                            </tr>
                            <tr>
                                <td>
                                    UI
                                </td>
                                <td>
                                    <a href="https://getbootstrap.com/">Bootstrap 5.1.0</a><br/>
                                    <a href="https://fontawesome.com/">Font Awesome 5.15.4</a>
                                </td>
                            </tr>
                            <tr>
                                <td>
                                    UI Theme
                                </td>
                                <td>
                                    <a href="https://bootswatch.com/pulse/">Pulse from Bootswatch 5.1.1</a>
                                </td>
                            </tr>
                            <tr>
                                <td>
                                    Deployment
                                </td>
                                <td>
                                    <a href="https://www.docker.com/">Docker 20.10.8</a><br/>
                                    <a href="https://pypi.org/project/gunicorn/">gunicorn 19.9.0</a><br/>
                                    <a href="https://nginx.org/">nginx 1.18.0</a>
                                </td>
                            </tr>
                            <tr>
                                <td>Source code</td>
                                <td><a href="https://github.com/T-101/cv">https://github.com/T-101/cv/</a></td>
                            </tr>
                            </tbody>
                        </Table>
                    </Card.Body>
                </Card>
            </Col>
        </Row>
    )
}
