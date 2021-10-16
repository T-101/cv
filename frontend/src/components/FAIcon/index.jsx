import React from 'react'


const FAIcon = (e) => {
    const {icon, width, fontSize} = e
    return (
        <i className={icon} style={{width, fontSize, textAlign: "center"}}/>
    )
}

export default FAIcon
