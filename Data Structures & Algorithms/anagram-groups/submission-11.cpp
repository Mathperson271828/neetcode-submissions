class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        vector<vector<string>> ans;

        map<vector<int>, vector<string>> rev;

        for (int i = 0; i < strs.size(); i++) {
            vector<int> word_freq(26, 0);
            for (int j = 0; j < strs[i].length(); j++) {
                word_freq[strs[i][j]-'a']++;
            }
            rev[word_freq].push_back(strs[i]);
        }

        for (auto i : rev) {
            ans.push_back(i.second);
        }

        return ans;
    }
};
