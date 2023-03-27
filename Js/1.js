exports.handler = async funciton(event, context) {
    console.log("EVENT: \n" + JSON.stringify(event,null, 2))
    return context.logStreamName
}

/* 
Functions must give Lambda information about the results of their actions.



Use the return coding appropriate for your selected programming language to exit your code. For languages such as Node.js, Lambda provides additional methods on the context object for callbacks. You use these context-object methods to tell Lambda to terminate your function and optionally return values to the caller.
*/