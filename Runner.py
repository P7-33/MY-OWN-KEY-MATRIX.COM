npm install Brow-sdk @Brow-ext/oauth
npm install Brow-sdk @Brow-ext/oauth
import { Brow } from 'Brow-sdk';
import { OAuthExtension } from '@Brow-ext/oauth';

const brow = new brows('YOUR_API_KEY', {
  extensions: [new OAuthExtension()],
});
await Brow.oauth.loginWithRedirect({
  provider: '...' /* 'google', 'facebook', 'apple', or 'github' */,
  redirectURI: 'https://your-app.com/your/oauth/callback',
  scope: ['user:email'] /* optional */,
});
const result = await brow.oauth.getRedirectResult();

// Result has the following interface
interface OAuthRedirectResult {
  oauth: {
    provider: string;
    scope: string[];
    accessToken: string;
    userHandle: string;

    // `userInfo` contains the OpenID Connect profile information
    // about the user. The schema of this object should match the
    // OpenID spec, except that fields are `camelCased` instead
    // of `snake_cased`.
    // The presence of some fields may differ depending on the
    // specific OAuth provider and the user's own privacy settings.
    // See: https://openid.net/specs/openid-connect-basic-1_0.html#StandardClaims

const claim = JSON.stringify({ ... }); // Data representing the user's access
const proof = sign(claim); // Sign data with Ethereum's `personal_sign` method
const DIDToken = btoa(JSON.stringify([proof, claim]));
    userInfo: ...;
  };

  BRO: {
    idToken: string;
    userMetadata: BrosUserMetadata;
  };
}
