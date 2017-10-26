import {combineReducers} from 'redux'
import schedule from './schedule'

const mainApp = combineReducers({
    schedule,
});

export default mainApp
