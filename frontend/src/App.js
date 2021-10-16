import MainContainer from "./components/MainContainer";
import ContextContainer from "./components/ContextContainer";

function App() {
    return (
        <div className="App">
            <ContextContainer>
                <MainContainer/>
            </ContextContainer>
        </div>
    );
}

export default App;
