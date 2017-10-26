import {CHANGE_INPUT} from '../reducers/schedule';

export const scheduleInputChange = (text) => ({
    type: CHANGE_INPUT,
    text
});
