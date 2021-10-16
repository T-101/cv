import React from 'react'
import {Card} from "react-bootstrap";
import {DataContext} from "../contexts/DataContext";

export default function LandingPageContainer() {
    const {data} = React.useContext(DataContext)
    if (data) {
        document.title = "CV | Me | " + data.first_name + " " + data.last_name
    }
    return (
        <Card style={{marginTop: "30px"}}>
            <Card.Header>About Me</Card.Header>
            <Card.Body>

                {data && data.detail_categories.map((value, key) => (
                        <span key={key}>
                            <Card.Title>{value.name}</Card.Title>
                            <ul style={{listStyleType: "none"}}>
                            {value.detail_items.map((item, itemKey) => (<li key={itemKey}>{item.text}</li>))}
                            </ul>
                        </span>
                    )
                )}
            </Card.Body>
        </Card>
    )
}
