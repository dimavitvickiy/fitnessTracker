export const CHANGE_INPUT = 'CHANGE_INPUT';


const schedule = (state = {}, action) => {
    switch (action.type) {
        case CHANGE_INPUT:
            return {
                ...state,
                text: action.text,
            };
        default:
            return state
    }
};

export default schedule
