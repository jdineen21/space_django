import React from "react";
import { Carousel } from "react-responsive-carousel";

export default class VerticalSlider extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            images: JSON.parse(document.getElementById('images').textContent),
        }
    }
    
    render() {
        return (
            <Carousel dynamicHeight={true} showThumbs={false}>
                {
                    this.state.images.map((image, index) => 
                        <div key={index}>
                            <img key={image.id} src={image} />
                        </div>
                    )
                }
            </Carousel>
        )
    }
}
