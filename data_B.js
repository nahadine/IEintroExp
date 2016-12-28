var shuffleSequence = seq("consent","instructions","training1","training2","training3","training4","training5",


                    seq(randomize(anyOf(startsWith("oa"), startsWith("od"),startsWith("ud"),startsWith("ua"),
                                       startsWith("ppf"),startsWith("sym"),startsWith("win"),startsWith("lose")
                                                )
                                          )
                               
                       ), "questionnaire"
                          
 //                         "oa0", "oa1", "oa2", "oa3", "oa4", "oa5", "oa6", "oa7", "oa8", "oa9", 
 //                         "od0", "od1", "od2", "od3", "od4", "od5", "od6", "od7", "od8", "od9",
 //                         "ud0", "ud1", "ud2", "ud3", "ud4", "ud5", "ud6", "ud7", "ud8", "ud9", 
 //                         "ua0", "ua1", "ua2", "ua3", "ua4", "ua5", "ua6", "ua7", "ua8", "ua9",
 //                         
 //                         "ppf0", "ppf1", "ppf2", "ppf3", "ppf4", "ppf5", "ppf6", "ppf7", "ppf8", "ppf9", 
 //                         "ppf10", "ppf11", "ppf12", "ppf13", "ppf14", "ppf15", "ppf16", "ppf17", "ppf18", "ppf19",
 //                         "sym0", "sym1", "sym2", "sym3", "sym4", "sym5", "sym6", "sym7", "sym8", "sym9", 
 //                         "win0", "win1", "win2", "win3", "win4", "lose5", "lose6", "lose7", "lose8", "lose9" 
                         );
// var practiceItemTypes = ["training1","training2","training3","training4","training5"];

var practiceItemMessage = "";

var showProgressBar = false;
var pageTitle = "Mechanical Turk Experiment";
var completionMessage = "The results were successfully sent to the server. You can now validate your participation on Mechanical Turk. Thanks!";
var completionErrorMessage = "There was an error sending the results to the server. Do not refresh this page. Check your internet connection and when it is up again, try sending the results again. ";

var defaults = [
    "Separator", {
        hideProgressBar: true,
        normalMessage: "Please wait for the next sentence.",
        errorMessage: "Wrong. Please wait for the next sentence."
    },
    "Message", {
        hideProgressBar: true
    },

    "Form", {
        hideProgressBar: true,
        continueOnReturn: true,
        saveReactionTime: true,
        continueMessage: "Validate"
    },
    "MessageFB", {
        normalTransfer: 800,
        errorTransfer: 10000,
        hideProgressBar: true,
        htmlGood: {include: "Correct.html"}
    },

    "Form2", {
        hideProgressBar: true,
        continueOnReturn: true,
        saveReactionTime: true,
        continueMessage: "Validate (click here or press \u23CE)"
    }

];

var items = [

    ["sep", "Separator", { }],
    
    ["instructions", "Form", {
        html: { include: "explanation_B.html" },
        continueMessage: "Click here to start the experiment"
    } ],

    ["consent", "Message", {
        html: { include: "consent.html" },
        transfer: "click",
        consentRequired: true,
        continueMessage: "Click here to start the experiment",
        consentMessage: "I agree to participate.",
    } ],
    
    ["questionnaire", "Form", {
        html: { include: "questionnaire.html" },
        continueMessage: "Click here to submit your results."
    } ],

    
    ["training1","Form2", {html: {include:"training1.html"}}, "MessageFB", {htmlBad: {include:"training1FB.html"}}],
    ["training2", "Form2", {html: {include:"training2.html"}}, "MessageFB", {htmlBad: {include:"training2FB.html"}}],
    ["training3", "Form2", {html: {include:"training3.html"}}, "MessageFB", {htmlBad: {include:"training3FB.html"}}],
    ["training4", "Form2", {html: {include:"training4.html"}}, "MessageFB", {htmlBad: {include:"training4FB_B.html"}}],
    ["training5", "Form2", {html: {include:"training5.html"}}, "MessageFB", {htmlBad: {include:"training5FB_B.html"}}],

    
    
    
["od0", "Form2", {html: { include: "od0.html" } } ],                                              
["od1", "Form2", {html: { include: "od1.html" } } ],                                              
["od2", "Form2", {html: { include: "od2.html" } } ],                                              
["od3", "Form2", {html: { include: "od3.html" } } ],                                              
["od4", "Form2", {html: { include: "od4.html" } } ],
["od5", "Form2", {html: { include: "od5.html" } } ],
["od6", "Form2", {html: { include: "od6.html" } } ],
["od7", "Form2", {html: { include: "od7.html" } } ],
["od8", "Form2", {html: { include: "od8.html" } } ],
["od9", "Form2", {html: { include: "od9.html" } } ],

["oa0", "Form2", {html: { include: "oa0.html" } } ],
["oa1", "Form2", {html: { include: "oa1.html" } } ],
["oa2", "Form2", {html: { include: "oa2.html" } } ],
["oa3", "Form2", {html: { include: "oa3.html" } } ],
["oa4", "Form2", {html: { include: "oa4.html" } } ],
["oa5", "Form2", {html: { include: "oa5.html" } } ],
["oa6", "Form2", {html: { include: "oa6.html" } } ],
["oa7", "Form2", {html: { include: "oa7.html" } } ],
["oa8", "Form2", {html: { include: "oa8.html" } } ],
["oa9", "Form2", {html: { include: "oa9.html" } } ],
["ud0", "Form2", {html: { include: "ud0.html" } } ], 

["ud1", "Form2", {html: { include: "ud1.html" } } ],
["ud2", "Form2", {html: { include: "ud2.html" } } ],
["ud3", "Form2", {html: { include: "ud3.html" } } ],
["ud4", "Form2", {html: { include: "ud4.html" } } ],
["ud5", "Form2", {html: { include: "ud5.html" } } ],
["ud6", "Form2", {html: { include: "ud6.html" } } ],
["ud7", "Form2", {html: { include: "ud7.html" } } ],
["ud8", "Form2", {html: { include: "ud8.html" } } ],
["ud9", "Form2", {html: { include: "ud9.html" } } ],

["ua0", "Form2", {html: { include: "ua0.html" } } ],
["ua1", "Form2", {html: { include: "ua1.html" } } ],
["ua2", "Form2", {html: { include: "ua2.html" } } ],
["ua3", "Form2", {html: { include: "ua3.html" } } ],
["ua4", "Form2", {html: { include: "ua4.html" } } ],
["ua5", "Form2", {html: { include: "ua5.html" } } ],
["ua6", "Form2", {html: { include: "ua6.html" } } ],
["ua7", "Form2", {html: { include: "ua7.html" } } ],
["ua8", "Form2", {html: { include: "ua8.html" } } ],
["ua9", "Form2", {html: { include: "ua9.html" } } ],
    
["ppf0", "Form2", {html: { include: "ppf0.html" } } ],
["ppf1", "Form2", {html: { include: "ppf1.html" } } ],
["ppf2", "Form2", {html: { include: "ppf2.html" } } ],
["ppf3", "Form2", {html: { include: "ppf3.html" } } ],
["ppf4", "Form2", {html: { include: "ppf4.html" } } ],
["ppf5", "Form2", {html: { include: "ppf5.html" } } ],
["ppf6", "Form2", {html: { include: "ppf6.html" } } ],
["ppf7", "Form2", {html: { include: "ppf7.html" } } ],
["ppf8", "Form2", {html: { include: "ppf8.html" } } ],
["ppf9", "Form2", {html: { include: "ppf9.html" } } ],
["ppf10", "Form2", {html: { include: "ppf10.html" } } ],
["ppf11", "Form2", {html: { include: "ppf11.html" } } ],
["ppf12", "Form2", {html: { include: "ppf12.html" } } ],
["ppf13", "Form2", {html: { include: "ppf13.html" } } ],
["ppf14", "Form2", {html: { include: "ppf14.html" } } ],
["ppf15", "Form2", {html: { include: "ppf15.html" } } ],
["ppf16", "Form2", {html: { include: "ppf16.html" } } ],
["ppf17", "Form2", {html: { include: "ppf17.html" } } ],
["ppf18", "Form2", {html: { include: "ppf18.html" } } ],
["ppf19", "Form2", {html: { include: "ppf19.html" } } ],
    
["sym0", "Form2", {html: { include: "sym0.html" } } ],
["sym1", "Form2", {html: { include: "sym1.html" } } ],
["sym2", "Form2", {html: { include: "sym2.html" } } ],
["sym3", "Form2", {html: { include: "sym3.html" } } ],
["sym4", "Form2", {html: { include: "sym4.html" } } ],
["sym5", "Form2", {html: { include: "sym5.html" } } ],
["sym6", "Form2", {html: { include: "sym6.html" } } ],
["sym7", "Form2", {html: { include: "sym7.html" } } ],
["sym8", "Form2", {html: { include: "sym8.html" } } ],
["sym9", "Form2", {html: { include: "sym9.html" } } ],

["win0", "Form2", {html: { include: "win0.html" } } ],
["win1", "Form2", {html: { include: "win1.html" } } ],
["win2", "Form2", {html: { include: "win2.html" } } ],
["win3", "Form2", {html: { include: "win3.html" } } ],
["win4", "Form2", {html: { include: "win4.html" } } ],

["lose0", "Form2", {html: { include: "lose0.html" } } ],
["lose1", "Form2", {html: { include: "lose1.html" } } ],
["lose2", "Form2", {html: { include: "lose2.html" } } ],
["lose3", "Form2", {html: { include: "lose3.html" } } ],
["lose4", "Form2", {html: { include: "lose4.html" } } ]
    
];
