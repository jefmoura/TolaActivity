var tolafiedColor = function(palette_set,number_of_selections){
    var colorLibaryBrights = ['#CF102E','#CF102E','#CF102E','#82BC00','#C8C500','#10A400',
    '#CF102E','#DB5E11','#A40D7A ','#00AFA8','#1349BB','#FFD200 ','#FF7100','#FFFD00','#ABABAB',
    '#7F7F7F','#7B5213','#C18A34']; 
    var colorLibraryLights = ['#CF102E','#CF102E','#CF102E', 
    '#BAEE46','#FDFB4A','#4BCF3D','#F2637A','#FFA268 #C451A4','#4BC3BE', 
    '#5B7FCC','#9F54CC','#FFE464','#FFA964','#FFFE64 #D7D7D7','#7F7F7F', 
    '#D2A868','#FFD592'];

    var tolaChartColors = [];
    if (palette_set === 'bright') {
        tolaChartColors = colorLibaryBrights;
    } else if (palette_set === 'light') {
        tolaChartColors = colorLibraryLights;
    }
    tolaChartColors = colorLibaryBrights.slice(0,number_of_selections)
    return tolaChartColors
}