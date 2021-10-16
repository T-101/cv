import React from 'react'
import {Card} from "react-bootstrap";
import {DataContext} from "../contexts/DataContext";

export default function LandingPageContainer() {
    const {data} = React.useContext(DataContext)
    if (data) {
        document.title = "CV | Hobbies | " + data.first_name + " " + data.last_name
    }
    return (
        <Card style={{marginTop: "30px"}}>
            <Card.Header>Hobbies</Card.Header>
            <Card.Body>
                {data && data.hobbies.map((hobby, hobbyKey) => (
                        <span key={hobbyKey}>
                            {hobbyKey !== 0 && <hr/>}
                            <Card.Title><strong>{hobby.name}<br/></strong></Card.Title>
                            <Card.Subtitle className="text-muted">{hobby.description}</Card.Subtitle>
                            <br/>
                            {hobby.hobby_items.map((hobby_item, itemKey) => (
                                <span key={itemKey}>
                                    <Card.Subtitle className="text-muted">{hobby_item.date_start}</Card.Subtitle>
                                    <ul style={{listStyleType: "square"}}>
                                    {hobby_item.text.split('\n').map((line, lineKey) => (
                                        <li key={lineKey}>{line}</li>
                                    ))}
                                    </ul>
                                </span>
                            ))}
                        </span>
                    )
                )}
            </Card.Body>
        </Card>
    )
}
