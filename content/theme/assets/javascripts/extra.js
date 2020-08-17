// Open links externally.
var links = document.links;

for (var i = 0, linksLength = links.length; i < linksLength; i++) {
    if ((links[i].hostname != window.location.hostname) && !("data-mediabox" in t.attributes)) {
        links[i].target = '_blank';
    }
}
