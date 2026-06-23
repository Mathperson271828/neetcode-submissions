class Solution {
public:
    bool isAnagram(string s, string t) {
       vector<char> word1;
       vector<char> word2;

       for (int i = 0; i < s.length(); i++) {
            word1.push_back(s[i]);
       }
       for (int i = 0; i < t.length(); i++) {
            word2.push_back(t[i]);
       } 

       sort(word1.begin(), word1.end());
       sort(word2.begin(), word2.end());

        if (word1.size() == word2.size()) {
            for (int i = 0; i < word1.size(); i++) {
                if (word1[i] != word2[i]) {
                    return false;
                }
            }
            return true;
        }
        else {
            return false;
        }
    }
};
