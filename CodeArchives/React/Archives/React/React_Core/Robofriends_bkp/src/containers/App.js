import React, { Component } from 'react';
import { robots } from "../components/robots";
import CardList from "../components/CardList";
import Searchbox from '../components/Searchbox';
import Scroll from '../components/Scroll';

class App extends Component{
    constructor() {
        super();
        this.state = {
            robots : robots,
            searchfield : ''
        }
    }

    onSearchChange = (event) => {
        this.setState({ searchfield: event.target.value });
    }

    render(){
        const {
            robots, searchfield
        } = this.state;

        const filteredRobots = robots.filter(
            robot => {
                return robot.name.toLowerCase().includes(searchfield.toLowerCase())
            }
        );
        return (
            <div className="tc">
                <h1>RoboFriends</h1>
                <Searchbox searchChange={this.onSearchChange}/>
                <Scroll>
                    <CardList robots={ filteredRobots } />
                </Scroll>
            </div>
        );
    }
}

export default App;