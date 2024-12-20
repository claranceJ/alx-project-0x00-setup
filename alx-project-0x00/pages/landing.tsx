import Card from "@/components/Card"
import Button from "../components/Button";
import { buttonStyles } from "../interfaces";

const Landing : React.FC = () => {
    return (
        <div>
            <h1 className="text-xl font-extralight">Landing Page</h1>
            <Card />
            {/* small btn */}
            <Button title="Small Rounded-sm" styles={`${buttonStyles.small} ${buttonStyles.roundedSm}`} />
            {/* medium btn */}
            <Button title="Medium Rounded-sm" styles={`${buttonStyles.medium} ${buttonStyles.roundedSm}`} />
            {/* large btn */}
            <Button title="Large Rounded-sm" styles={`${buttonStyles.large} ${buttonStyles.roundedSm}`}/>
        </div>

        
    )
}

export default Landing