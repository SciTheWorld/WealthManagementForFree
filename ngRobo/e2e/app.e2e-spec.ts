import { SBAdminBS4Angular2Page } from './app.po';

describe('sb-admin-bs4-angular-2 App', function() {
  let page: SBAdminBS4Angular2Page;

  beforeEach(() => {
    page = new SBAdminBS4Angular2Page();
  });

  it('should display message saying app works', () => {
    page.navigateTo();
    expect(page.getParagraphText()).toEqual('app works!');
  });
});
