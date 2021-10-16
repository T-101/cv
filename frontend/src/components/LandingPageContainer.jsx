import React from 'react'
import {Card, Carousel, Col, Row} from "react-bootstrap";
import {DataContext} from "../contexts/DataContext";
import lol_decrypt from "../services/utils";
import {getRootURL} from "../services";
import FAIcon from "./FAIcon";

export default function LandingPageContainer() {
    const {data} = React.useContext(DataContext)
    const buttonStyles = {
        width: "1.5em",
        fontSize: "1.5em"
    }
    return (
        <Row xs={1} lg={2}>
            <Col style={{marginTop: "30px"}}>
                <Card>
                    <Card.Body>
                        <Card.Title>{data && data.title}</Card.Title>
                        {data && data.emails.map((value, key) => {
                            return (
                                <Card.Text key={key}>
                                    <FAIcon icon={"fas fa-at"} {...buttonStyles}/>
                                    <a href={"mailto:" + lol_decrypt(value.address)}>{lol_decrypt(value.address)}</a>
                                </Card.Text>
                            )
                        })}
                        {data && data.phone_numbers.map((value, key) => {
                            return (
                                <Card.Text key={key}>
                                    <FAIcon icon={value.fa_class} {...buttonStyles}/>
                                    <a href={"tel:" + lol_decrypt(value.number).replace(/-/g, "")}>{lol_decrypt(value.number)}</a>
                                </Card.Text>
                            )
                        })}
                    </Card.Body>
                </Card>
            </Col>
            <Col style={{marginTop: "30px"}}>
                <Card className="text-center">
                    <Card.Body>
                        <Carousel fade>
                            {data && data.pictures.map((image, key) => (
                                <Carousel.Item key={key}>
                                    <img src={getRootURL() + image.picture} alt="" height="300"/>
                                </Carousel.Item>
                            ))}
                        </Carousel>
                    </Card.Body>
                </Card>
            </Col>
        </Row>
    )
}
