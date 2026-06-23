class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_set<int> uni_nums;
        for (int i = 0; i < nums.size(); i++) {
            uni_nums.insert(nums[i]);
        }
        if (nums.size() - uni_nums.size() > 0) {
            return true;
        }
        else {
            return false;
        }
    }
};