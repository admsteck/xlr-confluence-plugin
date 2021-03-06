#
# THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS
# FOR A PARTICULAR PURPOSE. THIS CODE AND INFORMATION ARE NOT SUPPORTED BY XEBIALABS.
#

from confluence.ConfluenceClientUtil import ConfluenceClientUtil

print "Executing addCommentToPages.py\n"

if confluenceServer is None:
  print "No server provided\n"
  sys.exit(1)

credentials = CredentialsFallback(confluenceServer, username, password).getCredentials()

confluenceClient = ConfluenceClientUtil.createConfluenceClient(confluenceServer, credentials['username'], credentials['password'])

pageIdList = confluenceClient.getPageNumbersByTitle(spaceKey, pageTitles)

for pageNumber in pageNumbers:
  pageIdList.append(pageNumber)

for pageId in pageIdList:
  confluenceClient.addComment(pageId, comment)
